def GET_people(BASE_URL=BASE_URL):
    people_url = BASE_URL + "people"
    people_json = requests.get(people_url).json()
    return people_json

def GET_films(BASE_URL=BASE_URL):
    films_url = BASE_URL + "films"
    films_json = requests.get(films_url).json()
    return movies_json

