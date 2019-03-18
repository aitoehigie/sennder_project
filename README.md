

This documentation details the process involved in solving the Sennder Python Developer test. The sections are as below:
1.) About the project
2.) Setup Instructions
3.) Details of tech stack
    * Reasons behind the choice of items in the tech stack.
4.) Details of the HTTP endpoints, methods,  arguments passed in and results returned.
5.) Details of how the search function as implemented works.
    * HTTP method used
    ** Endpoint created for the search function
6.) TODOs
7.) License
    



### About The Project
This project contains software written in Python as a solution to the Python Developer test by the candidate:
Name: Ehigie Pascal Aito
Email: <aitoehigie@gmail.com>
Date: 03/11/2019

### Setup & Installation Instruction

```sh
$ pipenv --python 3.7
$ pipenv shell
$ pipenv run pip install -r requirements.txt
$ gunicorn app:api --reload
```
The commands above will install all the dev dependencies in the "requirements.txt", configure the Python flask API.
Navigate to <http://localhost:5000/films> to start interacting with the API endpoints.

## Tech stack 
- Flask Microframework
- Gunicorn (a battle test WSGI server that runs the API [api.py]): this is a production ready WSGI server and is better than anything I could have written myself.
- Ratelimiting library to prevent abuse from consummers of the API. This limits requests to 5 requests/15 minutes.
- WSGI CORS Middleware library: I incorporated this into my REST API framework to enable Cross Site Origin Requests. As CORS is the standard way to do cross domain AJAX calls (for browsers that support it).


#### Caching
- lru_cache decorator from the functools standard Python library. I used this to decorate all the HTTP endpoints so subsequent HTTP requests receive a faster response because the initial response has been cached. The reason for choosing it is for speedups.

#### Testing
- I used py.test to create test cases, fixtures and clients to test the HTTP endpoints.


#### REST API HTTP ENDPOINTS
| Name   | Method     | URL Protected     |
| :------------- | :----------: | -----------: |
|  List | GET /films    | No    |


These endpoints return valid JSON objects as returns from the callbacks which is stored in a local file and also displayed in a HTML template albeit without styling. Any method not supported by each endpoint will return an error if called.
Supported REST methods are:
* GET



### Todos

 - Write MORE Tests.
 - Add async support.
 - Page styling.
 - Task Queue (Celer.y and Redis)
 - 
License
----

MIT


**Free Software, Hell Yeah!**
