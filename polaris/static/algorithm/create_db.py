"""
SCRIPT TO GENERATE BUS INFORMATION DATABASE

Database Plan: Maintain one table of each stop along with associated
information. Note that the time field represents the number of minutes 
after 6 AM the bus stops at a given point, so Night Safety Shuttle stops during
the early hours of the day will be treated as belonging to the previous calendar
day.
"""
import sqlite3

stop_count = 0 # To serve as each stop's unique ID.

def initialize_db():
    connection = sqlite3.connect('bus_data.db')
    controller = connection.cursor()
    controller.execute('''CREATE TABLE stops (uid INTEGER PRIMARY KEY, 
                          location TEXT, time INTEGER, line TEXT, days TEXT)''')
    return connection, controller

def load_h_line(controller):
    global stop_count
    insert_string = "INSERT INTO stops VALUES (?,?,?,'H Line', 'ALL')"

    for i in range(100, 756):
        if i % 30 == 10 or i % 30 == 5 and i > 120 and i != 756:
            controller.execute(insert_string, (stop_count, 'EVANS', i))
            stop_count += 1

        elif i % 30 == 15 or i % 30 == 1 and i > 120:
            controller.execute(insert_string, (stop_count, 'SCRA', i))
            stop_count += 1

        elif i % 30 == 17 or i % 30 == 29:
            controller.execute(insert_string, (stop_count, 'UCBG', i))
            stop_count += 1

        elif i % 30 == 19 or i % 30 == 27:
            controller.execute(insert_string, (stop_count, 'LHS', i))
            stop_count += 1

        elif i % 30 == 21 or i % 30 == 25:
            controller.execute(insert_string, (stop_count, 'SSL', i))
            stop_count += 1

    controller.execute(insert_string, (stop_count, 'BART', 95))
    stop_count += 1

    controller.execute(insert_string, (stop_count, 'BART', 775))
    stop_count += 1

    controller.execute(insert_string, (stop_count, 'BART', 760))
    stop_count += 1
    
    controller.execute(insert_string, (stop_count, 'BART', 806))
    stop_count += 1

    controller.execute(insert_string, (stop_count, 'EVANS', 780))
    stop_count += 1

    controller.execute(insert_string, (stop_count, 'SCRA', 782))
    stop_count += 1
    
    controller.execute(insert_string, (stop_count, 'UCBG', 784))
    stop_count += 1
    
    controller.execute(insert_string, (stop_count, 'LHS', 786))
    stop_count += 1

    controller.execute(insert_string, (stop_count, 'SSL', 790))
    stop_count += 1

    controller.execute(insert_string, (stop_count, 'SSL', 795))
    stop_count += 1

    controller.execute(insert_string, (stop_count, 'LHS', 797))
    stop_count += 1
    
    controller.execute(insert_string, (stop_count, 'UCBG', 799))
    stop_count += 1

    controller.execute(insert_string, (stop_count, 'SCRA', 801))
    stop_count += 1

    controller.execute(insert_string, (stop_count, 'EVANS', 803))
    stop_count += 1

def load_perimeter_line(controller):
    global stop_count
    insert_string = "INSERT INTO stops VALUES (?,?,?,'Perimeter Line', 'ALL')"
    for i in range(60, 781):
        if i % 30 == 0:
            controller.execute(insert_string, (stop_count, 'BART', i))
            stop_count += 1
        elif i % 30 == 2:
            controller.execute(insert_string, (stop_count, 'OXFU', i))
            stop_count += 1
        elif i % 30 == 4:
            controller.execute(insert_string, (stop_count, 'TOLMAN', i))
            stop_count += 1
        elif i % 30 == 5:
            controller.execute(insert_string, (stop_count, 'NORTH', i))
            stop_count += 1
        elif i % 30 == 6:
            controller.execute(insert_string, (stop_count, 'CORY', i))
            stop_count += 1
        elif i % 30 == 8:
            controller.execute(insert_string, (stop_count, 'EVANS', i))
            stop_count += 1
        elif i % 30 == 10:
            controller.execute(insert_string, (stop_count, 'STADIUM', i))
            stop_count += 1
        elif i % 30 == 11:
            controller.execute(insert_string, (stop_count, 'HAAS', i))
            stop_count += 1
        elif i % 30 == 12:
            controller.execute(insert_string, (stop_count, 'IHOUSE', i))
            stop_count += 1
        elif i % 30 == 14:
            controller.execute(insert_string, (stop_count, 'PIEDCHA', i))
            stop_count += 1
        elif i % 30 == 18:
            controller.execute(insert_string, (stop_count, 'COLHA', i))
            stop_count += 1
        elif i % 30 == 20:
            controller.execute(insert_string, (stop_count, 'KROEBER', i))
            stop_count += 1
        elif i % 30 == 21:
            controller.execute(insert_string, (stop_count, 'HEARST', i))
            stop_count += 1
        elif i % 30 == 23:
            controller.execute(insert_string, (stop_count, 'SPROUL', i))
            stop_count += 1
        elif i % 30 == 25:
            controller.execute(insert_string, (stop_count, 'RSF', i))
            stop_count += 1
        elif i % 30 == 27:
            controller.execute(insert_string, (stop_count, 'BANWAY', i))
            stop_count += 1
        elif i % 30 == 28:
            controller.execute(insert_string, (stop_count, 'SHAKIT', i))
            stop_count += 1

def load_central_line(controller):
    global stop_count
    insert_string = "INSERT INTO stops VALUES (?,?,?,'Central Line', 'ALL')"
    for i in range(45, 303):
        if i % 20 == 5:
            controller.execute(insert_string, (stop_count, 'BART', i))
            stop_count += 1
        elif i % 20 == 2:
            controller.execute(insert_string, (stop_count, 'OXFU', i))
            stop_count += 1
        elif i % 20 == 9:
            controller.execute(insert_string, (stop_count, 'TOLMAN', i))
            stop_count += 1
        elif i % 20 == 11:
            controller.execute(insert_string, (stop_count, 'NORTH', i))
            stop_count += 1
        elif i % 20 == 12:
            controller.execute(insert_string, (stop_count, 'CORY', i))
            stop_count += 1
        elif i % 20 == 15:
            controller.execute(insert_string, (stop_count, 'EVANS', i))
            stop_count += 1
        elif i % 20 == 18:
            controller.execute(insert_string, (stop_count, 'MOFFIT', i))
            stop_count += 1
        elif i % 20 == 0 and i > 45:
            controller.execute(insert_string, (stop_count, 'WEST', i))
            stop_count += 1
        elif i % 20 == 2 and i > 45:
            controller.execute(insert_string, (stop_count, 'LKS', i))
            stop_count += 1
    for i in range(615, 795):
        if i % 20 == 15:
            controller.execute(insert_string, (stop_count, 'BART', i))
            stop_count += 1
        elif i % 20 == 17:
            controller.execute(insert_string, (stop_count, 'OXFU', i))
            stop_count += 1
        elif i % 20 == 19:
            controller.execute(insert_string, (stop_count, 'TOLMAN', i))
            stop_count += 1
        elif i % 20 == 1:
            controller.execute(insert_string, (stop_count, 'NORTH', i))
            stop_count += 1
        elif i % 20 == 2:
            controller.execute(insert_string, (stop_count, 'CORY', i))
            stop_count += 1
        elif i % 20 == 5:
            controller.execute(insert_string, (stop_count, 'EVANS', i))
            stop_count += 1
        elif i % 20 == 8:
            controller.execute(insert_string, (stop_count, 'MOFFIT', i))
            stop_count += 1
        elif i % 20 == 10 and i > 45:
            controller.execute(insert_string, (stop_count, 'WEST', i))
            stop_count += 1
        elif i % 20 == 12 and i > 45:
            controller.execute(insert_string, (stop_count, 'LKS', i))
            stop_count += 1

def load_northside(controller):
    global stop_count
    insert_string = "INSERT INTO stops VALUES (?,?,?,'Northside Shuttle', 'WEEK')"
    for i in range(825, 1241):
        if i % 30 == 15:
            controller.execute(insert_string, (stop_count, 'MOFFITM', i))
            stop_count += 1
        elif i % 30 == 16:
            controller.execute(insert_string, (stop_count, 'LSA', i))
            stop_count += 1
        elif i % 30 == 17:
            controller.execute(insert_string, (stop_count, 'LKS', i))
            stop_count += 1
        elif i % 30 == 20:
            controller.execute(insert_string, (stop_count, 'BART', i))
            stop_count += 1
        elif i % 30 == 21:
            controller.execute(insert_string, (stop_count, 'USHA', i))
            stop_count += 1
        elif i % 30 == 23:
            controller.execute(insert_string, (stop_count, 'TOLMAN', i))
            stop_count += 1
        elif i % 30 == 24:
            controller.execute(insert_string, (stop_count, 'NORTH', i))
            stop_count += 1
        elif i % 30 == 25:
            controller.execute(insert_string, (stop_count, 'CORY', i))
            stop_count += 1
        elif i % 30 == 26:
            controller.execute(insert_string, (stop_count, 'FOOTHILL', i))
            stop_count += 1
        elif i % 30 == 27:
            controller.execute(insert_string, (stop_count, 'HIRIDGE', i))
            stop_count += 1
        elif i % 30 == 28:
            controller.execute(insert_string, (stop_count, 'EAST', i))
            stop_count += 1
        elif i % 30 == 29:
            controller.execute(insert_string, (stop_count, 'BOWLES', i))
            stop_count += 1
        elif i % 30 == 0:
            controller.execute(insert_string, (stop_count, 'HAAS', i))
            stop_count += 1
        elif i % 30 == 1:
            controller.execute(insert_string, (stop_count, 'IHOUSE', i))
            stop_count += 1
        elif i % 30 == 2:
            controller.execute(insert_string, (stop_count, 'KROEBER', i))
            stop_count += 1
        elif i % 30 == 3:
            controller.execute(insert_string, (stop_count, 'HEARST', i))
            stop_count += 1
        elif i % 30 == 4:
            controller.execute(insert_string, (stop_count, 'ASUC', i))
            stop_count += 1
        elif i % 30 == 5:
            controller.execute(insert_string, (stop_count, 'RSF', i))
            stop_count += 1
        elif i % 30 == 6:
            controller.execute(insert_string, (stop_count, 'BASHA', i))
            stop_count += 1
        elif i % 30 == 7:
            controller.execute(insert_string, (stop_count, 'BAKIT', i))
            stop_count += 1
        elif i % 30 == 8:
            controller.execute(insert_string, (stop_count, 'BART', i))
            stop_count += 1
        elif i % 30 == 9:
            controller.execute(insert_string, (stop_count, 'LKS', i))
            stop_count += 1
        elif i % 30 == 10:
            controller.execute(insert_string, (stop_count, 'LSA', i))
            stop_count += 1
        elif i % 30 == 11:
            controller.execute(insert_string, (stop_count, 'EVANS', i))
            stop_count += 1

def load_northside_saturday(controller):
    global stop_count
    insert_string = "INSERT INTO stops VALUES (?,?,?,'Northside Shuttle', 'SATURDAY')"
    for i in range(765, 1241):
        if i % 30 == 15:
            controller.execute(insert_string, (stop_count, 'MOFFITM', i))
            stop_count += 1
        elif i % 30 == 16:
            controller.execute(insert_string, (stop_count, 'LSA', i))
            stop_count += 1
        elif i % 30 == 17:
            controller.execute(insert_string, (stop_count, 'LKS', i))
            stop_count += 1
        elif i % 30 == 20:
            controller.execute(insert_string, (stop_count, 'BART', i))
            stop_count += 1
        elif i % 30 == 21:
            controller.execute(insert_string, (stop_count, 'USHA', i))
            stop_count += 1
        elif i % 30 == 23:
            controller.execute(insert_string, (stop_count, 'TOLMAN', i))
            stop_count += 1
        elif i % 30 == 24:
            controller.execute(insert_string, (stop_count, 'NORTH', i))
            stop_count += 1
        elif i % 30 == 25:
            controller.execute(insert_string, (stop_count, 'CORY', i))
            stop_count += 1
        elif i % 30 == 26:
            controller.execute(insert_string, (stop_count, 'FOOTHILL', i))
            stop_count += 1
        elif i % 30 == 27:
            controller.execute(insert_string, (stop_count, 'HIRIDGE', i))
            stop_count += 1
        elif i % 30 == 28:
            controller.execute(insert_string, (stop_count, 'EAST', i))
            stop_count += 1
        elif i % 30 == 29:
            controller.execute(insert_string, (stop_count, 'BOWLES', i))
            stop_count += 1
        elif i % 30 == 0:
            controller.execute(insert_string, (stop_count, 'HAAS', i))
            stop_count += 1
        elif i % 30 == 1:
            controller.execute(insert_string, (stop_count, 'IHOUSE', i))
            stop_count += 1
        elif i % 30 == 2:
            controller.execute(insert_string, (stop_count, 'KROEBER', i))
            stop_count += 1
        elif i % 30 == 3:
            controller.execute(insert_string, (stop_count, 'HEARST', i))
            stop_count += 1
        elif i % 30 == 4:
            controller.execute(insert_string, (stop_count, 'ASUC', i))
            stop_count += 1
        elif i % 30 == 5:
            controller.execute(insert_string, (stop_count, 'RSF', i))
            stop_count += 1
        elif i % 30 == 6:
            controller.execute(insert_string, (stop_count, 'BASHA', i))
            stop_count += 1
        elif i % 30 == 7:
            controller.execute(insert_string, (stop_count, 'BAKIT', i))
            stop_count += 1
        elif i % 30 == 8:
            controller.execute(insert_string, (stop_count, 'BART', i))
            stop_count += 1
        elif i % 30 == 9:
            controller.execute(insert_string, (stop_count, 'LKS', i))
            stop_count += 1
        elif i % 30 == 10:
            controller.execute(insert_string, (stop_count, 'LSA', i))
            stop_count += 1
        elif i % 30 == 11:
            controller.execute(insert_string, (stop_count, 'EVANS', i))
            stop_count += 1


def load_northside_sunday(controller):
    global stop_count
    line_count = 0
    insert_string = "INSERT INTO stops VALUES (?,?,?,'Northside Shuttle', 'SUNDAY')"
    for i in range(765, 1241):
        if i % 30 == 15:
            controller.execute(insert_string, (stop_count, 'MOFFITM', i))
            stop_count += 1
        elif i % 30 == 16:
            controller.execute(insert_string, (stop_count, 'LSA', i))
            stop_count += 1
        elif i % 30 == 17:
            controller.execute(insert_string, (stop_count, 'LKS', i))
            stop_count += 1
        elif i % 30 == 20:
            controller.execute(insert_string, (stop_count, 'BART', i))
            stop_count += 1
        elif i % 30 == 21:
            controller.execute(insert_string, (stop_count, 'USHA', i))
            stop_count += 1
        elif i % 30 == 23:
            controller.execute(insert_string, (stop_count, 'TOLMAN', i))
            stop_count += 1
        elif i % 30 == 24:
            controller.execute(insert_string, (stop_count, 'NORTH', i))
            stop_count += 1
        elif i % 30 == 25:
            controller.execute(insert_string, (stop_count, 'CORY', i))
            stop_count += 1
        elif i % 30 == 26:
            controller.execute(insert_string, (stop_count, 'FOOTHILL', i))
            stop_count += 1
        elif i % 30 == 27:
            controller.execute(insert_string, (stop_count, 'HIRIDGE', i))
            stop_count += 1
        elif i % 30 == 28:
            controller.execute(insert_string, (stop_count, 'EAST', i))
            stop_count += 1
        elif i % 30 == 29:
            controller.execute(insert_string, (stop_count, 'BOWLES', i))
            stop_count += 1
        elif i % 30 == 0:
            controller.execute(insert_string, (stop_count, 'HAAS', i))
            stop_count += 1
        elif i % 30 == 1:
            controller.execute(insert_string, (stop_count, 'IHOUSE', i))
            stop_count += 1
        elif i % 30 == 2:
            controller.execute(insert_string, (stop_count, 'KROEBER', i))
            stop_count += 1
        elif i % 30 == 3:
            controller.execute(insert_string, (stop_count, 'HEARST', i))
            stop_count += 1
        elif i % 30 == 4:
            controller.execute(insert_string, (stop_count, 'ASUC', i))
            stop_count += 1
        elif i % 30 == 5:
            controller.execute(insert_string, (stop_count, 'RSF', i))
            stop_count += 1
        elif i % 30 == 6:
            controller.execute(insert_string, (stop_count, 'BASHA', i))
            stop_count += 1
        elif i % 30 == 7:
            controller.execute(insert_string, (stop_count, 'BAKIT', i))
            stop_count += 1
        elif i % 30 == 8:
            controller.execute(insert_string, (stop_count, 'BART', i))
            stop_count += 1
        elif i % 30 == 9:
            controller.execute(insert_string, (stop_count, 'LKS', i))
            stop_count += 1
        elif i % 30 == 10:
            controller.execute(insert_string, (stop_count, 'LSA', i))
            stop_count += 1
        elif i % 30 == 11:
            controller.execute(insert_string, (stop_count, 'EVANS', i))
            stop_count += 1

def load_southside(controller):
    # Note for future expansion or updates: The method of loading stops into the
    # database is much better as used in this function than in the other
    # functions in this file.

    global stop_count

    locations = [('MOFFITM', 0), ('LSA', 1), ('WC', 2), ('BART', 5), 
                 ('SHAAL', 7), ('SHAKIT', 8), ('MANV', 9), ('DWIFU', 10), 
                 ('ELCHA', 11), ('UN3', 12), ('UN1', 13), ('UN2', 14), 
                 ('WAPIE', 15), ('CKC', 16), ('WACHA', 17), ('WABA', 18), 
                 ('IHOUSE', 19), ('HAAS', 20), ('GREEK', 21), 
                 ('FOOTHILL', 22), ('EVANS', 23), ('MOFFITM', 24)]
    week_times = [810] + [840 + 15*i for i in range(28)]
    sat_times = [750, 780] + [810 + 15*i for i in range(29)] + [1260, 1290,
                                                                1320]
    sun_times = [750 + 30*i for i in range(17)]

    insert_string = "INSERT INTO stops VALUES (?,?,?,?, 'WEEK')"
    for start in week_times:
        for location, time in locations:
            controller.execute(insert_string, (stop_count, location, start +
                                               time, "Southside Shuttle " + str(start)))
            stop_count += 1

    insert_string = "INSERT INTO stops VALUES (?,?,?,?, 'SATURDAY')"
    for start in sat_times:
        for location, time in locations:
            controller.execute(insert_string, (stop_count, location, start +
                                               time, "Southside Shuttle " + str(start)))
            stop_count += 1

    insert_string = "INSERT INTO stops VALUES (?,?,?,?, 'SUNDAY')"
    for start in sun_times:
        for location, time in locations:
            controller.execute(insert_string, (stop_count, location, start +
                                               time, "Southside Shuttle " + str(start)))
            stop_count += 1
    
def create_neighbors(controller):
    create_string = "CREATE TABLE Neighbor{0} AS SELECT * FROM stops WHERE time > ? \
                     AND location=? AND days=?"
    select_string = '''SELECT * FROM stops WHERE line=? AND time >? AND days=?'''
    insert_string = '''INSERT INTO {0} VALUES (?,?,?,?,?)'''

    stops = controller.execute('SELECT * FROM stops').fetchall()
    for stop in stops:
        controller.execute(create_string.format(stop[0]), (stop[2], stop[1],
                           stop[4]))
        controller.execute(select_string, (stop[3], stop[2], stop[4]))    
        next_stop = controller.fetchone()
        if next_stop:
            controller.execute(insert_string.format("Neighbor" + str(stop[0])), next_stop)


if __name__ == "__main__":
    connection, controller = initialize_db()
    load_h_line(controller)
    load_perimeter_line(controller)
    load_central_line(controller)
    load_northside(controller)
    load_northside_sunday(controller)
    load_northside_saturday(controller)
    load_southside(controller)
    create_neighbors(controller)
    connection.commit()
    connection.close()

