
import flask
from flask import request, jsonify
from flask_cors import CORS
import json
import requests



app = flask.Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
#app.config["DEBUG"] = True







@app.errorhandler(404)
def page_not_found(e):
    # your processing here
    link = request.url.replace('localhost:7777/','localhost:7777/')
    req = requests.get(link)
    return req

app.run()

