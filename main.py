from flask import Flask

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return "Hello! Welcome to mi casa!"


@app.route("/<username>")
def contact(username):
    return f"Hello {username} how are you doing"


app.run(host="0.0.0.0")
