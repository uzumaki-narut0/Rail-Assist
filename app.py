import os
import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_game():
    # welcome_msg = render_template('welcome')
    return question("What do you want me to do?")


@ask.intent("FetchMyPnrStatus")
def fetch_my_pnr_status():
    return statement("for the night is dark and full of terrors")

port = int(os.getenv('PORT', 5000))
app.run(debug=False, port=port, host='0.0.0.0')