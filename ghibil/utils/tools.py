import requests

BASE_URL = "https://ghibliapi.herokuapp.com/"

def fetch_movies_and_actors():
    results = [(item["title"], [requests.get(i).json()["name"] for i in item["people"] if len(item["people"]) > 1]) for item in requests.get("https://ghibliapi.herokuapp.com/films").json()] 
    return results

def headers_to_fs():
    with open("headers.txt", "r") as file:
        headers = file.readline()
        return headers
    





