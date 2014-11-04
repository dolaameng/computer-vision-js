from flask import Flask 
import flask
from os import path 

app = Flask(__name__)

@app.route('/')
def main_page():
    return flask.render_template("index.html")

if __name__ == "__main__":
	app.run(port = 1234, debug=True)