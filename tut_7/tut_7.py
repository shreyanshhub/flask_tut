from flask import Flask,render_template,redirect,url_for,request,session,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.cofig["SQL_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQL_TRACK_MODIFICATIONS"] = False
app.secret_key = "shreyansh__"

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column("name",db.String(100))
    email = db.Column("email",db.String(100))

    def __init__(self,name,email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/<name>")
def user(name):
    email = None
    if "user_name" in session:
        name = session["user_name"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=name).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html",name=name,email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user_name = request.form["nm"]
        session["user_name"] = user_name
        found_user = users.query.filter_by(name=username).first()
        
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user_name,"")
            db.session.add(usr)
            db.session.commit()

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
    session.pop("email",None)
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run()