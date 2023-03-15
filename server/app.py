#!/usr/bin/env python3

import os   # Importing the os module for file-related operations

from flask import Flask, request, current_app, g, make_response   # Importing Flask and related modules

app = Flask(__name__) # Creating an instance of the Flask class with the name of the current module

@app.before_request # Creating a function to be executed before the request is processed by the server
def app_path():                      
    g.path = os.path.abspath(os.getcwd())   # Getting the absolute path of the current working directory and storing it in a Flask global object, g

@app.route('/') # Creating a route decorator to define the route of the index page
def index(): # Creating a function to define the behavior of the index page
    host = request.headers.get('Host')  # Getting the value of the Host header from the incoming request and storing it in a variable
    appname = current_app.name # Getting the name of the Flask application instance and storing it in a variable

    response_body = f'''                # Creating a formatted string to be returned as the response body of the page
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    status_code = 200 # Defining a status code of 200 for the response
    headers = {}  # Creating an empty dictionary for the response headers

    return make_response(response_body, status_code, headers) # Creating a response object using the make_response function and returning it

if __name__ == '__main__': # Checking if the current module is being run as the main program
    app.run(port=5555, debug=True) # Running the Flask application on port 5555 with debug mode enabled