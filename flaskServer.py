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
	
@app.route("/bord1/<int:seqNum>", methods=['GET', 'PUT'])
def bord1(seqNum):
    printSequenceNum(0, seqNum)
    if request.method == 'GET':
        return get_logic("test", collection, seqNum)
    elif request.method == 'PUT':
        return put_test_logic("test", collection, seqNum)	
	
@app.route("/bord2/<int:seqNum>", methods=['GET', 'PUT'])
def bord2(seqNum):
    printSequenceNum(1, seqNum)
    if request.method == 'GET':
        return get_logic("test", collection, seqNum)
    elif request.method == 'PUT':
        return put_test_logic("test", collection, seqNum)

@app.route("/bord3/<int:seqNum>", methods=['GET', 'PUT'])
def bord3(seqNum):
    printSequenceNum(2, seqNum)
    if request.method == 'GET':
        return get_logic("test", collection, seqNum)
    elif request.method == 'PUT':
        return put_test_logic("test", collection, seqNum)

@app.route("/stat1/<int:seqNum>", methods=['PUT'])
def stat1(seqNum):
    printSequenceNum(0, seqNum)
    if request.method == 'PUT':
        return stat_logic(collection, seqNum)

@app.route("/stat2/<int:seqNum>", methods=['PUT'])
def stat2(seqNum):
    printSequenceNum1, seqNum)
    if request.method == 'PUT':
        return stat_logic(collection, seqNum)

@app.route("/stat3/<int:seqNum>", methods=['PUT'])
def stat3(seqNum):
    printSequenceNum(2, seqNum)
    if request.method == 'PUT':
        return stat_logic(collection, seqNum)

@app.errorhandler(404)
def not_found(error=None):
    request_logic(False)
    reply_logic(False)
    return buildError(404)
	
@app.errorhandler(400)
def not_found(error=None):
    request_logic(False)
    reply_logic(False)
    return buildError(400)

#########################################################
#                    APP ROUTES - END
#########################################################


if __name__ == '__main__':
    app.run(debug = True,host='localhost',port = 5000)
    #app.run(debug = True, host = 'localhost', port = 5000, threaded=True)