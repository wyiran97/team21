import pymongo
from pymongo import MongoClient
from flaskServerLogic import *

#Default host and port
client = MongoClient('localhost', 27017)
#Get database "ECE4534_test" (or create it)
db = client['ECE4534_test']
collection = db['test_collection']


collection.insert_one({"name":"board1"})

collection.update_one({"name":"board1"},{"$set":{"a":1,"b":2,"c":3}})

test = collection.find_one({"name":"board1"})

if test
   print("%d,%d\n" % (test['a'],test['b']))
