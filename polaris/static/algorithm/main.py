#! /usr/local/bin/python3.4
"""
Implements functionality to find directions given a start time, day of the week,
location, and desired destination. This file also contains a
command-line interface for the application.
"""
import sqlite3
import os
from polaris.static.algorithm.map import Map
from polaris.static.algorithm.stop import Stop
from polaris.static.algorithm.codenames import codenames, reverse_codenames
from flask import url_for

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
DB_PATH = os.path.join(SITE_ROOT, "bus_data.db")

def generate_graph():
    myMap = Map()
    controller = sqlite3.connect(DB_PATH).cursor()
    stop_dict = {}
    stops = controller.execute('SELECT * FROM stops').fetchall()

    for stop in stops:
        curr_stop = Stop(stop[0], stop[1], stop[2], stop[3], stop[4])
        stop_dict[stop[0]] = curr_stop

    for stop in stops:
        table_name = "Neighbor" + str(stop[0])
        neighbors = controller.execute('SELECT * FROM {}'.format(table_name)).fetchall()
        for neighbor in neighbors:
            stop_dict[stop[0]].add_neighbor(stop_dict[neighbor[0]], neighbor[2]
                                            - stop[2])
    for stop in stop_dict.values():
        myMap.insert(stop)

    return myMap

def find_directions(start_time, day, start_loc, dest):
    graph = generate_graph()
    possible_starts, possible_ends = [], []
    controller = sqlite3.connect(DB_PATH).cursor()

    if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        day_option = 'WEEK'
    else:
        day_option = day.upper()
    controller.execute("SELECT * FROM stops WHERE time > ? AND time < ? AND location = \
                            ? AND (DAYS='ALL' or DAYS=?)", (start_time,
                                                           start_time + 45, start_loc, day_option))

    for start in controller.fetchall(): 
            possible_starts.append(start[0])

    controller.execute("SELECT * FROM stops WHERE time > ? AND time < ? and location = \
                            ?  AND (DAYS='ALL' or DAYS=?)", (start_time,
                                                             start_time + 60, dest, day_option))

    for end in controller.fetchall():
            possible_ends.append(end[0])
    possible_paths = []

    for i in possible_starts:
        for j in possible_ends:
            path = graph.find_path(graph.vertices[i], graph.vertices[j])
            if path:
                possible_paths.append((path, graph.vertices[j].time))
                    
    if possible_paths:
        curr_min = 1000000
        curr_path = []
        for path, time in possible_paths:
            if time < curr_min:
                curr_path = path
                curr_min = time

        result = []
        prev = curr_path[0]
        result.append(prev)
        for i in curr_path[1:]:
            if i.line != prev.line and not (i.line[:3] == 'Sou' and prev.line[:3] == 'Sou'):
                result.append(prev)
                result.append(i)
            prev = i

        result.append(curr_path[-1])

        for stop in result:
            stop.time = to_human_time(stop.time)
            if stop.line.startswith('Sou'):
                stop.line = stop.line[:17]
            stop.location = reverse_codenames[stop.location]
        
        tuples = []
        while result:
            enter = result.pop(0)
            exit = result.pop(0)
            tuples.append((enter, exit))

        return tuples

    else:
        return []

def to_human_time(time):
    time += 360
    if time >= 24 * 60:
        time -= 24 * 60
    minute = time % 60
    hour = time // 60
    if minute < 10:
        minute_str = '0' + str(minute)
    else:
        minute_str = str(minute)

    if hour < 10:
        hour_str = '0' + str(hour)
    else:
        hour_str = str(hour)

    return hour_str + ':' + minute_str

if __name__ == "__main__":
    start_time = input("Enter time (24 Hour): ").split(':')
    start_time = int(start_time[0]) * 60 + int(start_time[1]) - 360
    if start_time < 0:
        start_time += 24 * 60
    day = input("Enter day: ").lower()
    start_loc = input("Enter origin codename: ")
    dest = input("Enter destination codename: ")
    result = find_directions(start_time, day, start_loc, dest)
    if result:
        print("Path found:")
        print(result)
    else:
        print("Sorry. We could not find a path.")
