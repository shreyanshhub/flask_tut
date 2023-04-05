from flask import Flask,redirect,url_for,render_template
app = Flask(__main__)

@app.route("/<name>")
def hello(name):
  return render_template("index.html",name=name,radius=3.14)


if __name__ == "__main__":
  app.run()
