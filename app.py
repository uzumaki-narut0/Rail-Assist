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

@ask.launch
def new_request():
    return question("What do you want me to do?")

@ask.intent("RunningStatus")
def running_status():
    return statement("poo poo poo poo")

@ask.intent("FetchMyPnrStatus")
def fetch_my_pnr_status():
    return question('What is your PNR number?')

@ask.intent("PNRNumber")
def pnr_status(pnr_no):
    x = str(pnr_no);
    full_url = base_url + x + "/apikey/" + api_key;
    r = requests.get(full_url)
    json_data = r.json();
    return statement(json_data['passengers'][0]['current_status'])

port = int(os.getenv('PORT', 5000))
app.run(debug=False, port=port, host='0.0.0.0')