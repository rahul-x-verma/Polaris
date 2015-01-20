"""
A basic test to ensure the database was successfully populated.
"""
import sqlite3

controller = sqlite3.connect('bus_data.db').cursor()
controller.execute('SELECT * from stops')
row = controller.fetchone()
print(row)
controller.execute('SELECT * FROM Neighbor{0}'.format(row[0]))
print(controller.fetchall())
