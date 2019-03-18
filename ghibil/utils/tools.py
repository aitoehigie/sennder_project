import requests

BASE_URL = "https://ghibliapi.herokuapp.com/"


def fetch_movies_and_actors():
    """The below is a nifty list comprehension that retrieves all information from the films API endpoint and makes a GET request to retrieve information about all actors in each film"""

    results = [
        (
            item["title"],
            [
                requests.get(i).json()["name"]
                for i in item["people"]
                if len(item["people"]) > 1
            ],
        )
        for item in requests.get("https://ghibliapi.herokuapp.com/films").json()
    ]
    return results[0][0]


def headers_to_fs():
    with open("headers.txt", "r") as file:
        headers = file.readline()
        return headers
