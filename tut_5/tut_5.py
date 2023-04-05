from flask import Flask,render_template,redirect,url_for,request,session

app = Flask(__name__)
app.secret_key = "shreyansh__"

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/<name>")
def user(name):
    if "user_name" in session:
        name = session["user_name"]
        return render_template("user.html",name=name)
    else:
        return redirect(url_for("login"))

@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user_name = request.form["nm"]
        session["user_name"] = user_name
        return redirect(url_for("user"))
    else:
        if "user_name" in session:
            return redirect(url_for("user"))
            
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user_name",None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()