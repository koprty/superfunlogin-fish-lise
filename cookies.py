from flask import Flask,render_template,request
import utils

app=Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("index.html")
    else:
        u = request.form['uname']
        pswd = request.form['pswd']
        valid_user = utils.authenticate(uname,pswd)
        if button=="cancel" or not(valid_user):
            return render_template("login.html",l=l)
        else:
            return render_template("welcome.html",
                                   name=uname)
        
@app.route("/")
def welcome():
    return "<h1>Welcome %s</h1>"%("user")

@app.route("/register")
def register():

        return "<h1>Welcome %s</h1>"%(uname)

if __name__=="__main__":
   app.debug=True
   app.run(host="0.0.0.0",port=5000)
