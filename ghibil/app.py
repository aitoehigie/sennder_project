#!/usr/bin/env python

from functools import lru_cache
from flask import Flask, jsonify
from utils.tools import fetch_movies_and_actors, headers_to_fs
import requests

api = Flask(__name__)


@lru_cache(maxsize=256)
@api.route("/", methods=["GET"])
@api.route("/films", methods=["GET"])
@api.route("/films/", methods=["GET"])
def films():
    """
    This callback first checks if the Etag value returned by the requests.head is the same as the value on the file.
    If its the same, there will be no need to hit the external Ghibil API, it returns the value as stored locally in a text file called "data.txt".
    If its not the same value, then it executes the fetch_movies_and_actors function and returns the value.
    """
    if (
        requests.head("https://ghibliapi.herokuapp.com/films").headers.get("Etag")
        != headers_to_fs()
    ):
        films_json = fetch_movies_and_actors()
        with open("data.txt", "w") as file:
            file.write(f"{films_json}")
        with open("headers.txt", "w") as file:
            file.write(
                f'{requests.head("https://ghibliapi.herokuapp.com/films").headers.get("Etag")}'
            )
        return f"{films_json}"
    else:
        with open("data.txt", "r") as file:
            films_json = file.readlines()
        return f"{films_json}"
