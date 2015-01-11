from pprint import pprint

class Map():
    """
    Stores a map of the transit system in a graph data structure. Each vertex
    represents one bus stopping at a given geographical location. Each edge
    represents the time between one stop and the next (including waiting time if
    applicable).

    """
    def __init__(self):
        """           
        Creates an empty map.
        """
        self.adjacency_list = {}
        self.vertices = {}

    def insert(self, stop):
        """
        Adds a vertex and its neighbors to the graph.
        """
        self.vertices[stop.uid] = stop
        self.adjacency_list[stop] = {}
        for neighbor in stop.neighbors:
            self.adjacency_list[stop][neighbor[0]] = neighbor[1]

    def find_path(self, start, end):
        """
        Uses breadth-first search to find the buses necessary to go between two
        stops. 
        """
        S = [start]
        pi = {}

        while end not in pi.keys():
            if not S:
                return []
            curr = S.pop()
            for vertex in self.adjacency_list[curr]:
                if vertex not in pi.keys():
                    S.append(vertex)
                    pi[vertex] = curr

        if pi[end]:
            result = [end]
            while (start != end):
                end = pi[end]
                result = [end] + result
            return result
        else:
            return []

    def distance(self, v1, v2):
        return self.adjacency_list[v1][v2]
         
    def show(self):
        """
        Returns a human-readable version of the map.

        """
        pprint(self.adjacency_list)
