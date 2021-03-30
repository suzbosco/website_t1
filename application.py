from flask import Flask, redirect, url_for, render_template, request
from datetime import timedelta
import os

application = Flask(__name__, template_folder='templates', static_folder='img')
app = application
application.secret_key = os.urandom(24)
application.permanent_session_lifetime = timedelta(minutes=5)


#main page

@application.route('/')
def home():
    return render_template("index.html")

#@app.route("/<name>")
#def home(name):
 #   return render_template("index.html", content=name, t1=["bosco", "hugo", "on9jai"])

@application.route('/test')
def home1():
    return render_template("new.html")

@application.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user_session"] = user
        flash("Login Successful")
        return redirect(url_for("user_fun"))
    else:
        if "user_session" in session:
            flash("Already login")
            return redirect(url_for("user_fun"))

        return render_template("login.html")
    
@application.route("/user")
def user_fun():
    if "user_session" in session:
        user = session["user_session"]
        return render_template("user.html", user=user)
    else:
        flash("you are not login!")
        return redirect(url_for("login"))


@application.route("/logout")
def logout():
    if "user_session" in session:
        user = session["user_session"]
        flash(f"you have been logged out, {user}", "info")
    session.pop("user_session", None)

    return redirect(url_for("login"))




#redirect
@application.route('/admin')
def admin():
    return redirect(url_for("home1"))

if __name__ == "__main__":
    application.run()


