from flask import Flask, redirect, url_for, render_template, request

application = Flask(__name__)
app = application


#main page

@application.route('/')
def home():
    return render_template("templates/index.html")

#@app.route("/<name>")
#def home(name):
 #   return render_template("index.html", content=name, t1=["bosco", "hugo", "on9jai"])

#@application.route('/test')
#def home1():
 #   return render_template("new.html")




#redirect
#@application.route('/admin')
#def admin():
 #   return redirect(url_for("home1"))

if __name__ == "__main__":
    application.run()


