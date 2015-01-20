class Stop():
    """
    Represents a bus stopping at a certain time and place.
    """

    def __init__(self, uid, location, time, line, days):
        self.uid = uid
        self.location = location
        self.neighbors = []
        self.time = time
        self.line = line
        self.days = days

    def add_neighbor(self, neighbor, time):
        self.neighbors.append((neighbor, time))

    def __repr__(self):
        return "ID: {4}\nLocation: {0}\nTime: {1}\nLine: {2}\nDays: {3}".format(self.location,
                                                                                self.time, 
                                                                                self.line,
                                                                                self.days,
                                                                                self.uid)


