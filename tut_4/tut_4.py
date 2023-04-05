from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/<name>")
def user(name):
    return render_template("user.html",name=name)

@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user_name = request.form["nm"]
        return redirect(url_for("user",name=user_name))
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run()