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

# Main route, returns all posts and displays them in the index.html template
@app.route('/', methods=["GET"])
def main():
    posts = ndb.get_polls()
    return render_template("index.html", posts=posts)

@app.route('/add_page', methods=["GET"])
def add_page():
    return render_template("add.html")  

# Add a new poll, takes in a JSON POST request with just the title
@app.route('/add', methods=["POST"])
def add_poll():
    title = request.form['title']
    poll = ndb.create_poll(title)

    return redirect(url_for('main'))

# Delete a poll, takes in a JSON POST request with just the title
@app.route('/polls/<int:pid>/delete', methods=["GET"])
def delete_poll(pid):
    success = ndb.delete_poll(pid)

    
    if (success is not None):
        print('deleted poll success')
    else:
        print("bruh")
    return redirect(url_for('main'))


# View the poll's comments and results
@app.route('/polls/<int:pid>', methods=["GET"])
def poll_page(pid):
    post = ndb.get_poll(pid)
    comments = ndb.get_comments(pid)
    return render_template("comments.html", post=post, comments=comments, pid=pid)

# Add a comment
@app.route('/polls/<int:pid>', methods=["POST"])
def add_comment(pid):
    body = request.form['body']
    comments = ndb.add_comment(pid, body)

    return redirect(url_for('poll_page', pid=pid))