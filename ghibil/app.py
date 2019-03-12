#!/usr/bin/env python

import requests
from flask import Flask, render_template, url_for

app = Flask(__name__)
BASE_URL = "https://ghibliapi.herokuapp.com/"

@app.route("/", methods=["GET"])
@app.route("/movies", methods=["GET"])
@app.route("/movies/", methods=["GET"])
def movies():
    movies_json = GET_movies()
    return render_template("movies.html")

def GET_people(BASE_URL=BASE_URL):
    people_url = BASE_URL + "people"
    people_json = requests.get(people_url).json()
    return people_json

def GET_films(BASE_URL=BASE_URL):
    movies_url = BASE_URL + "films"
    movies_json = requests.get(movies_url).json()
    return movies_json
