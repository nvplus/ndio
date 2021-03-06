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

def get_poll(pid):
    q = "SELECT * FROM polls WHERE id={}".format(pid)
    return _do_query(q)

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

def get_comments(pid):
    #makes a poll, takes in a title
    q =  'SELECT * FROM comments WHERE pid={} ORDER BY date DESC'.format(pid)
    return _do_query(q)

def add_comment(pid:int, body:str):
    # add a comment to a specified poll
    
    date = datetime.datetime.now()
    q =  'INSERT INTO comments (pid, body, date) VALUES(?, ?, ?);'
    
    try:
        args = (pid, body, date)
        _do_query_commit(q, args)

        return _do_query('SELECT last_insert_rowid() FROM comments')
    except Exception as e:
        return "Could not add comment to poll: {}".format(e)


def delete_comments(pid:int):
    # cleanse a poll of comments
    
    q =  'DELETE FROM comments WHERE pid=?;'

    try:
        args = (pid)
        _do_query_commit(q, args)

        print(get_comments(pid))
        return get_comments(pid)
    except Exception as e:
        return "Could not delete comments: {}".format(e)

def delete_poll(pid:int):
    delete_comments(pid)

    q =  'DELETE FROM polls WHERE id=?;'
    
    try:
        args = (pid)
        _do_query_commit(q, args)

        return True
    except Exception as e:
        return "Could not delete poll: {}".format(e)

def search(term):
    q = 'SELECT * FROM polls WHERE title LIKE "%{}%"'.format(term)
    return _do_query(q)

def increment_yes(pid):
    q = "UPDATE polls SET yes = yes + 1 WHERE id={}".format(pid)
    _do_query_commit(q)
    return "ok"
    
def increment_no(pid):
    q = "UPDATE polls SET no = no + 1 WHERE id={}".format(pid)
    _do_query_commit(q)
    return "ok"