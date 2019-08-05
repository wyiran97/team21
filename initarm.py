import pymongo
import time
from pymongo import MongoClient
from flaskServerLogic import *

#Default host and port
client = MongoClient('localhost', 27017)
#Get database "ECE4534_test" (or create it)
db = client['ECE4534_test']
collection = db['test_collection']


collection.insert_one({"name":"arm"})

collection.update_one({"name":"arm"},{"$set":{"ARM_VALUE":4}})
