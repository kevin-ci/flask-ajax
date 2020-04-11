from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/vote/<direction>', methods=["GET"])
def vote(direction):
    return "Hello from Flask. You have voted " + direction


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
