#Name:         flaskServerLogic.py
#Written by:   Joseph Messou
#For:          ECE 4534, Virginia Tech
#Last update:  03/03/2019
#Comments:     Helper functions for the flask servers
from flask import Flask, jsonify, request, Response
from bson.json_util import dumps


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

#Goal:   Add an integer to a document in the database
#        Create the document if it doesn't exist
#Input:
#        -document_name: name of the document (string)
#        -collection: collection to add the document to (collection)
#Output: HTTP response (success or error)
def put_add_logic(document_name, collection):
    expected_length=2
    sumData = request.get_json()
    validData_nb = sum_put_checkData(sumData,expected_length)

    #Add to object or create object if necessary
    if validData_nb == expected_length:
        oldSum_cursor = collection.find({"name": document_name}).limit(1)
        oldSum = next(oldSum_cursor,None)
        if oldSum:
            newSum = oldSum["value"] + sumData["value"]
            collection.update_one({"name": document_name}, {"$set": {"value": newSum}})
        else:
            collection.insert_one(sumData)
        return Response("Sum Value Updated", status=201)
    else:
        error = {'status': BAD_REQUEST, 'error': 'Bad data for: ' + request.url}
        return buildError(error["status"],error)

#Goal:   Check that if the data received has the correct format
#        Correct: name = sum / value: integer
#Input:
#        -sumData: Data received (dict)
#        -expected_length: Expected length of the data (default to 2) (int)
#Output: Number of valid key/values in sumData (int)
def sum_put_checkData(sumData,expected_length=2):
    validData_nb = 0
    #Expecting name and integer
    if len(sumData) == expected_length:
        for key, value in sumData.items():
            if key == "name" and value == "sum":
                validData_nb = validData_nb + 1
            if key == "value" and isinstance(value, (int,float)):
                validData_nb = validData_nb + float(value).is_integer()
    return validData_nb
#########################################################
#                 HELPERS - SUM - START
#########################################################

#########################################################
#                 HELPERS - DEBUG - START
#########################################################
#Goal:   Append a payload to a document in the database
#        Create the document if it doesn't exist
#Input:
#        -document_name: name of the document (string)
#        -collection: collection to append the document to (collection)
#Output: HTTP response (success or error)
def put_append_logic(document_name, collection):
    debugData = request.get_json()

    #Add to object or create object if necessary
    if debugData:
        oldDebug_cursor = collection.find({"name": document_name}).limit(1)
        oldDebug = next(oldDebug_cursor,None)
        if oldDebug:
            collection.update_one({"name": document_name}, {"$set": debugData})
        else:
            debugData["name"] = "debug"
            collection.insert_one(debugData)
        return Response("Debug Value Updated", status=201)
    else:
        error = {'status': BAD_REQUEST, 'error': 'Bad data for: ' + request.url}
        return buildError(error["status"],error)

def sum_put_checkData(sumData,expected_length=2):
    validData_nb = 0
    #Expecting name and integer
    if len(sumData) == expected_length:
        for key, value in sumData.items():
            if key == "name" and value == "sum":
                validData_nb = validData_nb + 1
            if key == "value":
                validData_nb = validData_nb + float(value).is_integer()
    return validData_nb
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
def get_logic(document_name, collection):
    document = getDocument(document_name, collection)
    if document:
        document_json = dumps(document)
        #Send back HTTP response
        return Response(document_json, status=SUCCESS, mimetype='application/json')
    else:
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
