from flask import Flask, redirect, url_for, render_template, request

application = Flask(__name__, static_url_path='/otherstatic', static_folder=r'C:\Users\85265\PycharmProjects\website_test1\img')


#main page

@application.route("/")
def home():
    return render_template("index.html")

#@app.route("/<name>")
#def home(name):
 #   return render_template("index.html", content=name, t1=["bosco", "hugo", "on9jai"])

@application.route("/test")
def home1():
    return render_template("new.html")




#redirect
@application.route("/admin")
def admin():
    return redirect(url_for("home1"))

if __name__ == "__main__":
    application.run()


