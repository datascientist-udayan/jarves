import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
#cursor.execute(query)
#conn.commit()

query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()