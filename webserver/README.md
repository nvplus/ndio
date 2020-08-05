
# Ndio Backend

  This is the back-end code for Ndio. It is written Python using the Flask framework and uses SQLite3 for the database. The `backend` and `frontend`folders are deprecated and are only kept for legacy purposes.

## Using the server

1. Environment setup

 - Navigate to `flask-backend` and run the command`py3 -m venv venv`to create a virtual environment.
- Install Flask using `pip3 install flask`.
- Copy and paste `clean.db` into the root of your`flask-backend` folder, and rename it to `ndio.db`.

2. Running the server
- Run `venv\Scripts\activate` to start the virtual environment.
- Use `flask run` to start the server. It should start on localhost:5000. Use `CTRL + C` to stop the server.
- Once you are done, you may exit the virtual environment using `deactivate`.
