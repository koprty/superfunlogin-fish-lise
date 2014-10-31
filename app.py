from flask import Flask, render_template, request, redirect, url_for
from pymongo import Connection
from utils import adduser, authenticate

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="GET":
        #return "<h1>This is the login page</h1>"
        return render_template("index.html", message = "")
    else:
        global cur_user
        global cur_name
        username = request.form["username"]
        password = request.form["password"]
        button = request.form["b"]
        if button == "Login":
            validity = authenticate(username, password)
            if validity == "Valid":
                cur_user = username
                cur_name = get_name(username)
                return redirect(url_for('loggedin1'))
            else:
                #return "<h1>This is the login page</h1>"
                return render_template("index.html", message="Login unsuccessful")
        else:
            return redirect(url_for('register'))
        
@app.route("/logout")
def logout():
    return "<h1>This is the logout page</h1>"
    #return render_template("logout.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        #return "<h1>This is the register page</h1>"
        return render_template("register.html", message="")
    else:
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm_password"]
        name = request.form["name"]
        if (confirm == password):
            adduser(username,name,password)
            return redirect(url_for('login'))
        else:
            #return "<h1>This is the register page</h1>"
            return render_template("register.html", message = "Password doesn't match confirmation")
        
@app.route("/info")
def info():
    return "<h1>This is the info page</h1>"
    #return render_template("info.html")

@app.route("/loggedin1")
def loggedin1():
    return "<h1>This is the first logged in page</h1>"
    #return render_template("loggedin1.html")

@app.route("/loggedin2")
def loggedin2():
    return "<h1>This is the second logged in page</h1>"
    #return render_template("loggedin2.html")



if __name__=="__main__":
    conn = Connection()
    db = conn['1258']
    app.debug = True
    app.run()
