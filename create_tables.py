import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#Must be INTEGER
#This is the only place where int vs INTEGER matters in auto-incrementing columns

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)" #real is decimal point values
cursor.execute(create_table)

#cursor.execute("INSERT INTO items VALUES ('test', 10.99)")
connection.commit()
connection.close()