# file that interacts with the database 

import sqlite3 as sql 
from os import path 

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    print("Attempting to insert into database")
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    print("Data committed to database")
    con.close()



def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts 