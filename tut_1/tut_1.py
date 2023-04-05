from flask import Flask,redirect,url_for
app = Flask(__main__)

@app.route("/")
def hello():
  return "hey <h1>Home</h1>"

@app.route("/<name>")
def user(name):
  return f"Hey{name}"

@app.route("/admin")
def admin():
  return redirect(url_for("home")) #url_for("function_name")

if __name__ == "__main__":
  app.run()
