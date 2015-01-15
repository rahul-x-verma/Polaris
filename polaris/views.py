import sqlite3
from polaris import polaris
from flask import render_template, request
from polaris.static.algorithm.main import find_directions, DB_PATH
from polaris.static.algorithm.codenames import codenames, reverse_codenames
from datetime import datetime

@polaris.route('/')
@polaris.route('/index')
def index():
    controller =  sqlite3.connect(DB_PATH)
    now = datetime.now()
    weekday = datetime.today().weekday()
    hour = now.hour
    minute = now.minute
    time = hour * 60 + minute - 360

    if time < 0:
        time += 24 * 60
        weekday -= 1
    if weekday == 6:
        weekday = "SUNDAY"
    elif weekday == 5:
        weekday = "SATURDAY"
    else:
        weekday = "WEEK"

    possible_starts_tup = controller.execute("SELECT location FROM stops WHERE time \
                                          > ? and time < ?+ \
                                          45", (time, time)).fetchall()
    
    possible_ends_tup = controller.execute("SELECT location FROM stops WHERE time \
                                          > ? and time < ?+ \
                                          60", (time, time)).fetchall()
    possible_starts, possible_ends = [], []

    for start in possible_starts_tup:
        possible_starts.append(reverse_codenames[start[0]])
    for end in possible_ends_tup:
        possible_ends.append(reverse_codenames[end[0]])


    possible_starts = list(set(possible_starts))
    possible_ends = list(set(possible_ends))

#    if not possible_starts and possible_ends:
#        possible_starts, possible_ends = ["No lines currently in service."], ["No lines currently in service."] 
    return render_template('index.html', starts=possible_starts,
                            ends=possible_ends)

@polaris.route('/results', methods=['POST', 'GET'])
def results():
#    if request.method == 'GET':
#        return index()
    start = request.form.get('Start')
    dest = request.form.get('Destination')
    now = datetime.now()
    weekday = datetime.today().weekday()
    hour = now.hour
    minute = now.minute
    time = hour * 60 + minute - 360

    if time < 0:
        time += 24 * 60
        weekday -= 1
    if weekday == 6:
        weekday = "sunday"
    elif weekday == 5:
        weekday = "saturday"
    else:
        weekday = "monday"


    
    if start.startswith('Mof'):
        if time > 13 * 60:
            start_code = "MOFFITM"
        else:
            start_code = "MOFFIT"
    else:
        start_code = codenames[start]

    if dest.startswith('Mof'):
        if time > 13 * 60:
            end_code = "MOFFITM"
        else:
            end_code = "MOFFIT"
    else:
        end_code = codenames[dest]

    result = find_directions(time, weekday, start_code, end_code)
    if result:
        return render_template('results.html', results=result)
    else:
        return render_template('sorry.html')
