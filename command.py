r =  [(item["title"], item["people"]) for item in [requests.get(url["url"]).json() for url in [requests.get(url["url"]).json() for url in [requests.get(url).json() for url in [item["url"] for item in requests.get("https://ghibliapi.herokuapp.com/films").json()]]]]]


