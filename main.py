# An object of WSGI application
from flask import Flask, render_template
from flask import redirect, url_for, request
# Flask constructor
app = Flask(__name__)

# Which url i want to access


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_emotion")
def get_emotion():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)