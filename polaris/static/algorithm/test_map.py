"""
A basic test of the BFS path finding algorithm.
"""
from polaris.static.algorithm.map import Map
from polaris.static.algorithm.stop import Stop

ts = Stop(1, "Trafalgar Square", 0, 1, "ALL")
ws = Stop(2, "Wembley Stadium", 5, 1, "ALL")
tl = Stop(4, "Tower of London", 8, 2, "ALL")

ts.add_neighbor(ws, 5)

graph = Map()
graph.insert(ts)
graph.insert(ws)

print(graph.find_path(ts, ws))
