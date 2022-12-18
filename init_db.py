import sqlite3

connection=sqlite3.connect('database.db')
with open("/Users/franco/Documents/teststreamlit/flask pitone prog/crea_post.sql") as f:
    connection.executescript((f.read()))

connection.commit()
connection.close()