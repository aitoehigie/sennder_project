#!/usr/bin/env python

import requests
from flask import Flask, render_template, url_for
from utils.tools import GET_films, GET_people

app = Flask(__name__)
BASE_URL = "https://ghibliapi.herokuapp.com/"

@app.route("/", methods=["GET"])
@app.route("/movies", methods=["GET"])
@app.route("/movies/", methods=["GET"])
def films():
    movies_json = GET_films()
    return render_template("films.html")

