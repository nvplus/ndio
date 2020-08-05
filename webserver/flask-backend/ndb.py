from flask import g, request
import sqlite3
import datetime

DB_PATH = "ndio.db"

def get_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn

    except Exception as e:
        print("Could not connect to the database. Error: ", e)
        return None

def _do_query(query:str, args = (), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def _do_query_commit(query: str, args = ()):
    cur = g.db.execute(query, args)
    g.db.commit()

#rest stuff
def get_polls():
    return _do_query("SELECT * FROM polls ORDER BY date DESC")

def get_poll(pid:int):
    print(pid)
    return _do_query("SELECT * FROM polls WHERE id = '{}'".format(pid))

def create_poll(title: str):
    #makes a poll, takes in a title
    date = datetime.datetime.now()
    q =  'INSERT INTO polls (title, date) VALUES(?, ?);'
    
    try:
        args = (title, date)
        _do_query_commit(q, args)

        return _do_query('SELECT last_insert_rowid() FROM polls')
    except Exception as e:
        return "Could not insert poll: {}".format(e)

def get_comments(pid:int):
    #makes a poll, takes in a title
    print(pid)
    q =  'SELECT * FROM comments WHERE id="{}" ORDER BY date DESC'.format(pid)
    return _do_query(q)