#!/usr/bin/env python

#pip install flask
from flask import Flask, json, render_template, request
import os

#create instance of Flask app
app = Flask(__name__)

#decorator
#flask is calling a function called route
@app.route("/")
def echo_hello():
    return "<p>Hello World</p>"

@app.route("/gdp")
def gdp():
    json_url = os.path.join(app.static_folder,"","us_gdp.json")
    data_json = json.load(open(json_url))
    
    return render_template('index.html',data=data_json)

@app.route("/gdp/<year>")
def gdp_year(year):
    json_url = os.path.join(app.static_folder,"","us_gdp.json")
    data_json = json.load(open(json_url))


if __name__ == "__main__":
    app.run(debug=True)