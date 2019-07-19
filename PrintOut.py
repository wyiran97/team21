import pymongo
import time
from pymongo import MongoClient
from flaskServerLogic import *

#Default host and port
client = MongoClient('localhost', 27017)
#Get database "ECE4534_test" (or create it)
db = client['ECE4534_test']
collection = db['test_collection']


#collection.insert_one({"name":"server"})
#collection.insert_one({"name":"board1"})

#collection.update_one({"name":"server"},{"$set":{"serverRecieve":1,"serverMissRequest":2,"serverCorrectReply":3 ,"serverInCorrectReply":4}})
#collection.update_one({"name":"board1"},{"$set":{"requetSent":5,"correctReceive":6,"missReply":7 }})

while True:
      server = collection.find_one({"name":"server"})
      board = collection.find_one({"name":"board1"})
      if server and board:
            print(" Server: (serverRecieve: %d, serverMissRequest: %d , serverCorrectReply: %d, serverInCorrectReply: %d )\n " % (server['serverRecieve'],server['serverMissRequest'],server['serverCorrectReply'],server['serverInCorrectReply']))
            print(" Board:  (requetSent: %d , correctReceive: %d , missReply: %d) \n" % (board['requetSent'],board['correctReceive'],board['missReply']))
      time.sleep(1)
