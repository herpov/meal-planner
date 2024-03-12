import sqlite3 as lite

conn = lite.connect('test.db')
cur = conn.cursor()

def get_posts():
    with conn:
        cur.execute("SELECT * FROM table")
        print(cur.fetchall())

get_posts()