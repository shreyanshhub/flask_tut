from flask import Flask,render_template,redirect,url_for,request,session,flash

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
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user_name = request.form["nm"]
        session["user_name"] = user_name
        flash("Login Successful","info")
        return redirect(url_for("user"))
    else:
        if "user_name" in session:
            flash("Already logged in!","info")
            return redirect(url_for("user"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    if "user_name" in session:
        user_name = session["user_name"]
        flash("You have been logged out",{user_name},"info")

    session.pop("user_name",None)
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()