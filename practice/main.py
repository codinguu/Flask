from flask import Flask

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return "hello Flask"


@app.route("/<username>")
def contact(username):
    return f"hello {username}"


app.run(host="0.0.0.0")
