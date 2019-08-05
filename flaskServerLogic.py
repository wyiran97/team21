#Name:         flaskServerLogic.py
#Written by:   Joseph Messou
#For:          ECE 4534, Virginia Tech
#Last update:  03/03/2019
#Comments:     Helper functions for the flask servers
from flask import Flask, jsonify, request, Response
from bson.json_util import dumps

seqNumOf3Board = [0, 0, 0]
Stat_corRec = 0
Stat_inCorRec = 0
Stat_corReply = 0
Stat_inCorReply = 0
Stat_misReq = 0
#########################################################
#                    ERRORS - START
#########################################################
SUCCESS=200
CREATED=202
BAD_REQUEST=400
NOT_FOUND=404
#########################################################
#                   ERRORS - END
#########################################################

#########################################################
#                 HELPERS - SUM - START
#########################################################



def printSequenceNum(index, seqNum):
    global Stat_misReq
    global seqNumOf3Board
    seqNumOf3Board[index] += 1
    if seqNum - seqNumOf3Board[index] >= 1:
        print(seqNum)
        Stat_misReq += (seqNum - seqNumOf3Board[index])
        
    seqNumOf3Board[index] = seqNum
	
def request_logic(correct):
    global Stat_corRec
    global Stat_inCorRec
    if(correct == True):
        Stat_corRec += 1
    else:
        Stat_inCorRec += 1    
        

def reply_logic(correct):
    global Stat_corReply
    global Stat_inCorReply
    if(correct == True):
        Stat_corReply += 1
    else:
        Stat_inCorReply += 1

#Goal:   Add an integer to a document in the database
#        Create the document if it doesn't exist
#Input:
#        -document_name: name of the document (string)
#        -collection: collection to add the document to (collection)
#Output: HTTP response (success or error)
def put_test_logic(document_name, collection, seqNum):
    data = request.get_json()
    request_logic(True)
    seq = {"seq":seqNum}
    seq_json = dumps(seq)
    #Add to object or create object if necessary
    if data:
        value = data['ARM_VALUE']
        oldPut_cursor = collection.find({"name":document_name}).limit(1)
        oldPut = next(oldPut_cursor,None)
        if oldPut:
            collection.update_one({"name":document_name}, {"$set": {"ARM_VALUE":value}})
        else:
            collection.insert_one({"name":document_name,"ARM_VALUE":value})
        reply_logic(True)
        return Response(seq_json, status=201, mimetype='application/json')
    else:
        reply_logic(False)
        error = {'status': BAD_REQUEST, 'error': 'Bad data for: ' + request.url, 'seq': seqNum}
        return buildError(error["status"],error)

def stat_logic(collection, seqNum):
    statData = request.get_json()
    boardName = statData['name']
    reqSend = statData['requetSent']
    corRec = statData['correctReceive']
    missReply = statData['missReply']
    global Stat_corRec
    global Stat_inCorRec
    
    seq = {"seq":seqNum}
    seq_json = dumps(seq)
    
    serverStatData = {"name":"server","serverRecieve":Stat_corRec,"serverMissRequest":Stat_misReq,"serverCorrectReply":Stat_corReply,"serverInCorrectReply":Stat_inCorReply}

	#server statistic
    if serverStatData:
        server_cursor = collection.find({"name":"server"}).limit(1)
        server = next(server_cursor,None)
        if server:
            collection.update_one({"name":"server"}, {"$set": {"serverRecieve": Stat_corRec,"serverMissRequest": Stat_misReq,"serverCorrectReply": Stat_corReply,"serverInCorrectReply": Stat_inCorReply}})
        else:
            serverStatData["name"] = "server"
            collection.insert_one(serverStatData)
    else:
        error = {'status': BAD_REQUEST, 'error': 'Bad data for: ' + request.url}
    
    
    #PIC32 statistic
    if statData:
        oldDebug_cursor = collection.find({"name": boardName}).limit(1)
        oldDebug = next(oldDebug_cursor,None)
        if oldDebug:
            collection.update_one({"name": boardName}, {"$set": {"requetSent": reqSend,"correctReceive": corRec,"missReply": missReply}})
        else:
            statData["name"] = boardName
            collection.insert_one(statData)
        request_logic(True)
        return Response(seq_json, status=201, mimetype='application/json')
    else:
        request_logic(False)
        error = {'status': BAD_REQUEST, 'error': 'Bad data for: ' + request.url, 'seq': seqNum}
        return buildError(error["status"],error)
#########################################################
#                 HELPERS - DEBUG - START
#########################################################


#########################################################
#               OTHER HELPERS - START
#########################################################
#Goal:   Get document from the database as an HTTP Response
#Input:
#        -document_name: name of the document (string)
#        -collection: collection to get the document from (collection)
#Output: HTTP response with document or HTTP error
def get_logic(document_name, collection, seqNum):
    document = getDocument(document_name, collection)
    document.update({'seq':seqNum})
    if document.get("_id"):
        del document["_id"]
        
    request_logic(True)
    if document:
        document_json = dumps(document)
        #Send back HTTP response
        reply_logic(True)
        return Response(document_json, status=SUCCESS, mimetype='application/json')
    else:
        reply_logic(False)
        return buildError(NOT_FOUND)

#Goal:   Get unique document from the database
#Input:
#        -name: name of the document (string)
#        -collection: collection to get the document from
#Output:
#        -document (dict or None if not found)
def getDocument(name, collection):
    #Look for 1 document (there should only be 1 in the database)
    cursor = collection.find({"name": name}).limit(1)
    #You can also use a for loop that will run once
    return  next(cursor,None)

#Send an error
def buildError(status=NOT_FOUND,error=None):
    if error is None:
        error = {'status': status, 'error': 'Not Found: ' + request.url}
	#jsonify returns a flask.Response object
    resp = jsonify(error)
    resp.status_code = status

    return resp
#########################################################
#               OTHER HELPERS - END
#########################################################
