from flask import Flask, g, render_template, request, redirect, url_for, jsonify
import sqlite3
import ndb

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = ndb.get_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/polls/add/', methods=["POST"])
def create_poll():
    #takes in a title and creates a poll, formatted in json
    title = request.json.get('title')
    result = ndb.create_poll(title)

@app.route('/', methods=["GET"])
def keysets():
    result = ndb.get_polls()
    return render_template("index.html")

"""
@app.route('/posts/comments/, methods=["GET"])
def get_keyset(keyset_id):
    result = kkz_db.get_keyset(keyset_id)
    return result if result != None else "No keyset found with id {}".format(keyset_id) 

@app.route('/posts/comments/add, methods=["POST"])
def get_keyset(keyset_id):
    result = kkz_db.get_keyset(keyset_id)
    return result if result != None else "No keyset found with id {}".format(keyset_id) 
"""