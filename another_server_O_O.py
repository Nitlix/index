
import flask
from flask import request, jsonify
from flask_cors import CORS
import json
import sys
import uuid
import random
import time
import discord 
from discord.ui import Button


import requests
from nErrors import errors
from pyNit import valueCheck
from pyNit import random_with_N_digits



app = flask.Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
#app.config["DEBUG"] = True


main = {}
dir = "site-main/apps/games/"


with open(f'{dir}storage.json', 'r+') as o:
  main = json.load(o) 



def write(e):
    with open(f'{dir}storage.json', 'w+') as o:
        o.seek(0)
        json.dump(e, o, indent=4)
        o.truncate()
    return "Admin Panel - WRITE was successful. API Saves Saved."



def shutdown():
    print("Shutting down...")
    write(main)
    sys.exit
    return "Admin Panel - API Shut down."

def loggingswitch():
    print("Log toggled")

    if main['logging']:
        main['logging'] = False
    else:
        main['logging'] = True

    return "Admin Panel - Toggled Log Writing."

def throwError(error1):
    return jsonify({"OK": False,"code": str(error1),"resp": errors[error1]})

def throwResponce(responce1):
    return jsonify({"OK": True,"resp": responce1})

def checkValid(req):
    for x,a in req.args.items():
        if "&" in a or len(a) > 100:
            return True



    






@app.route('/', methods=['GET'])
def home():
    return jsonify("Hi! This is the Nitlix Data API! Thanks for somehow getting this link and coming here. I haven't seen a lot of people here for a long time you know...")



@app.route('/api/v1/', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    for x,y in request.args.items():
        if x == "method": 
            if y == "create":
                try: 
                    if request.args['object'] == "game":
                        
                        games[request.args['name']] = {}

                    if request.args['object'] == "game":
                        games[request.args['name']] = {}


                except Exception:
                    pass


@app.route('/api/v1/tower/', methods=['GET'])
def tower():
    if checkValid(request):
        return throwError("N10")
    action = None
    user = False
    if "action" in request.args and "value" in request.args:
        if "action" == "create-game":
            try:
                e = request.args['value']
                while True:
                    r = random_with_N_digits(6)
                    if r not in main['games']:
                        main['games'][r] = {"name": e['name'],"players":e['creator']}
                main['games']





app.run()
#if app.config["DEBUG"]:
#    app.run()
#elif __name__ == "__main__":
#    from waitress import serve
#    serve(app, host="0.0.0.0", port=8242)