from flask import Flask,render_template,request,url_for,redirect,session
import utils

app=Flask(__name__)
        
@app.route("/")
@app.route("/home")
def home():
    if request.method=="GET":
        return render_template("base.html")
    else:
        u = request.form.get('uname',None)
        pswd = request.form.get('pswd',None)
        valid_user = utils.authenticate(u,pswd)
        if not(valid_user) and not u == None:
            return render_template("base.html",msg=u)
        else:
            session['myuser'] = u
            return redirect(url_for('loggedin1'))
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("base.html")
    else:
        u = request.form.get('uname',None)
        pswd = request.form.get('pswd',None)
        valid_user = utils.authenticate(u,pswd)
        if not(valid_user):
            return render_template("base.html",msg=u)
        else:
            session['myuser'] = u
            print session
            return redirect(url_for('loggedin1'))
       #return render_template("index.html", name=u)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html",rconf="Getting register")
    else:
        ru = request.form.get('runame',None)
        rpswd = request.form.get('rpswd',None)
        print ru, rpswd
        if utils.adduser(ru,rpswd):
                return render_template("register.html", rconf="You have successfully registered.")
        else:
                return render_template("register.html", rconf="Username taken. Try Again.")
        
@app.route("/logout")
def logout():
    session.pop("myuser", None)
    return render_template("index.html")
@app.route("/info")
def info():
    return "<h1>This is the info page</h1>"

@app.route("/loggedin1")
def loggedin1():
    if "myuser" in session:
        return render_template("myindex.html")
    return render_template("login_error.html")

@app.route("/loggedin2")
def loggedin2():
    print session
    if "myuser" in session and not session["myuser"] == None :
        return render_template("myindex.html")
    return render_template("login_error.html")
    

if __name__=="__main__":
    app.secret_key="*]%4WQ4ki[uUF!3pZcNbM8_4SsDFSEsd"
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
