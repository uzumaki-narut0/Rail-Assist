#beiifc3h3m 
import os
import requests
import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
api_key = "beiifc3h3m";
base_url = "http://api.railwayapi.com/v2/pnr-status/pnr/";
pnr_no = str(6306534268);
full_url = base_url + pnr_no + "/apikey/" + api_key;
# json.loads()
@ask.launch
def new_request():
    return question("What do you want me to do?")

@ask.intent("RunningStatus")
def running_status():
    return statement("poo poo poo poo")

@ask.intent("FetchMyPnrStatus")
def fetch_my_pnr_status():
    print(full_url)
    r = requests.get(full_url)
    print(r.json())
    return statement("for the night is dark and full of terrors")

port = int(os.getenv('PORT', 5000))
app.run(debug=False, port=port, host='0.0.0.0')