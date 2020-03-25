import os, sys

import pyodbc

connection_string = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s;Uid=Admin;Pwd=;" % (os.path.abspath("test.mdb"))
print(connection_string)
db = pyodbc.connect(connection_string)

q = db.cursor()
for row in q.execute("SELECT TOP 10 * FROM Areas;"):
    print(row)

for row in q.execute("SELECT TOP 10 * FROM Motorways;"):
    print(row)
