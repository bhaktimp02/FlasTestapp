import flask
from flask import Flask, render_template
import sys
import os

app = Flask(__name__, template_folder='template')
print(os.path)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"


if __name__ == "__main__":

    app.run(port=5000, host= '127.0.0.1', debug=True)
