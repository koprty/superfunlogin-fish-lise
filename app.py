import pymongo
from flask import Flask, render_template
from pymongo import Connection

conn = Connection('localhost',1258)
app = Flask(__name__)

db = conn['pd7']

print db.collection_names()

@app.route("/")
@app.route("/login")
def login():
    return "<h1>This is the login page</h1>"

@app.route("/logout")
def logout():
    return "<h1>This is the logout page</h1>"

@app.route("/register")
def register():
    return "<h1>This is the register page</h1>"

@app.route("/info")
def info():
    return "<h1>This is the info page</h1>"

@app.route("/loggedin1")
def loggedin1():
    return "<h1>This is the first logged in page</h1>"

@app.route("/loggedin2")
def loggedin2():
    return "<h1>This is the second logged in page</h1>"



if __name__=="__main__":
    # set the instance variable debug to True
    app.debug = True
    # call the run method
    app.run()
