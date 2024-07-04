import sqlite3
conn= sqlite3.connect('database1.db')


cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    sn INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rollno INTEGER,
    results TEXT UNIQUE
    )
''')
conn.commit()



