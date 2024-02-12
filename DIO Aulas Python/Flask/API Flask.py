import pandas as pd 
from flask_ngrok import run_with_ngrok
from flask import (request,
                   jsonify,
                   Flask
                   )
import random as rk


app = Flask (__name__) # The name of the application name 

run_with_ngrok(app)

d = {
    "name": "Nikola",
    "surmane": "Tesla",
    "age": "50"
    }

@app.route("/") # code to assign HomePage URL in our aoo to function home.

def home():
    '''
    The entrie line below must be written in a single line.
    '''
    
    return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AN TO CHECK OUT PUT ADD '/output' TO THE URL.</hh3><"


@app.route("/input") # Code to assing Input URL in our appp to function input 

def input():
    return jsonify(d) # "d" is the dictionary we defined 

@app.route('/output', methods = ['GET', 'POST']) # output page 

def predJson():
    pred = run.choice(["positive", "negative"])
    nd = d # our input 
    nd ["prediction"] = pred
    
    return jsonify(nd)

app.run()

