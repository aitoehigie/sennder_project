#!/usr/bin/env python

from functools import lru_cache
from flask import Flask, jsonify, render_template
from utils.tools import fetch_movies_and_actors, headers_to_fs
import requests

api = Flask(__name__)


@lru_cache(maxsize=256)
@api.route("/", methods=["GET"])
@api.route("/films", methods=["GET"])
@api.route("/films/", methods=["GET"])
def films():
    """
    This callback first checks if the Etag value returned by the request HEAD is the same as the value on the file [headers.txt].
    If its the same, there will be no need to hit the external Ghibil API, it returns the value as stored locally in a text file called "data.txt".
    If its not the same value, then it executes the fetch_movies_and_actors function and returns the value.
    """
    if (
        requests.head("https://ghibliapi.herokuapp.com/films").headers.get("Etag")
        != headers_to_fs()
    ):
        films_json = fetch_movies_and_actors()[0][0]
        with open("data.txt", "w") as file:
            for line in films_json:
                file.writeline(line)
        with open("headers.txt", "w") as file:
            file.write(
                f'{requests.head("https://ghibliapi.herokuapp.com/films").headers.get("Etag")}'
            )
        return render_template("films.html", films_json=films_json)
    else:
        with open("data.txt", "r") as file:
            films_json = file.readlines()[0].split()
        return render_template("films.html", films_json=films_json)
