#Name:         flaskServer.py
#Goal:         Run a flask server at a fixed address/port with two main routes
#              (1) /sum: Add to object (document) in the database
#              (2) /debug: Append to object (document) in the database
#Written by:   Joseph Messou
#For:          ECE 4534, Virginia Tech
#Last update:  02/26/2019
#Comments:     Address: localhost / Port: 5000
#              Database: localhost:27017

from flask import Flask
app = Flask(__name__)
import pymongo
from pymongo import MongoClient
from flaskServerLogic import *

#Default host and port
client = MongoClient('localhost', 27017)
#Get database "ECE4534_test" (or create it)
db = client['ECE4534_test']
collection = db['test_collection']


#########################################################
#                   APP ROUTES - START
#########################################################
#Test your app with this (home)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sum", methods=['GET', 'PUT'])
def sum():
    if request.method == 'GET':
        return get_logic("sum", collection)
    elif request.method == 'PUT':
        return put_add_logic("sum", collection)

@app.route("/debug", methods=['GET', 'PUT'])
def debug():
    if request.method == 'GET':
        return get_logic("debug",collection)
    elif request.method == 'PUT':
        return put_append_logic("debug", collection)

@app.errorhandler(404)
def not_found(error=None):
    return buildError(404)

#########################################################
#                    APP ROUTES - END
#########################################################


if __name__ == '__main__':
    app.run(debug = True,host='localhost',port = 5000)
    #app.run(debug = True, host = 'localhost', port = 5000, threaded=True)
