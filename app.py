from flask import Flask,render_template,redirect
import sqlite3
#####to run the app go to terminal
####$ export FLASK_APP=app
##$ export FLASK_DEBUG=1
###$ flask run

app=Flask(__name__,template_folder='/Users/franco/Documents/teststreamlit/flask pitone prog/Templates')

@app.route("/")
def index():
    connection = sqlite3.connect('database.db')
    connection.row_factory=sqlite3.Row
    posts=connection.execute("SELECT * FROM posts").fetchall()
    connection.close()
    return render_template("index.html",posts=posts)

@app.route("/<int:idx>/delete",methods=("POST",))
def delete(idx):
    connection = sqlite3.connect('database.db')
    connection.row_factory=sqlite3.Row
    connection.execute("DELETE FROM posts WHERE id=?",(idx,)).fetchall()
    connection.commit()
    connection.close()
    return redirect("/")
