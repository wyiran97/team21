#!/usr/bin/env python3

"""
A simple echo client
"""
import clientKeys
import socket
import sys
from cryptography.fernet import Fernet
import hashlib
import pickle
from ibm_watson import TextToSpeechV1
from pygame import mixer
import tweepy
import time


host = sys.argv[2]
port = int(sys.argv[4])
size = int(sys.argv[6])
print("["+time.strftime("%H:%M:%S",time.localtime())+"][Checkpoint 01] Connecting to: " + sys.argv[2] + " on port " + sys.argv[4])


#capture tweet question
auth=tweepy.OAuthHandler(clientKeys.APIkey,clientKeys.APISkey)
auth.set_access_token(clientKeys.Accesstoken,clientKeys.AccessStoken)
api=tweepy.API(auth)



class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        str_text=status.text
        #exclude hash tag
        question=str_text.replace("#ECE4564T02","")
        print("["+time.strftime("%H:%M:%S",time.localtime())+"][Checkpoint 03] New Question: " + question)

        #construct payload part
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(question.encode())
        checksum = hashlib.md5(cipher_text).hexdigest()
        print("["+time.strftime("%H:%M:%S",time.localtime())+"][Checkpoint 04]Encrypt: Generated Key: " + key.decode() + "| Cipher text: " + cipher_text.decode())
        payload_tuple = (key, cipher_text, checksum)
        print("["+time.strftime("%H:%M:%S",time.localtime())+"][Checkpoint 05] Sending data: ")
        print(payload_tuple)
        payload_pickel = pickle.dumps(payload_tuple)
        s.send(payload_pickel)

        time.sleep(2)

        #parse answer payload
        data = s.recv(size)
        data_unpickle = pickle.loads(data)
        print("["+time.strftime("%H:%M:%S",time.localtime())+"][Checkpoint 06] Received data: ")
        print(data_unpickle)
        answer_cipher_text = data_unpickle[1]
        answer_cipher_suit = Fernet(data_unpickle[0])
        plain_answer = answer_cipher_suit.decrypt(answer_cipher_text)
        print("["+time.strftime("%H:%M:%S",time.localtime())+"][Checkpoint 07]Decrypt: Using Key: " + data_unpickle[0].decode() + "| Plain text: " + plain_answer.decode())


        #specks out answer
        text_to_speech = TextToSpeechV1(
            iam_apikey = clientKeys.client_watsonID(),
            url = clientKeys.client_watsonUrl()
        )

        with open('answer.mp3', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    plain_answer.decode(),
                    voice='en-US_AllisonVoice',
                    accept='audio/mp3'
                ).get_result().content)

        mixer.init()
        mixer.music.load('answer.mp3')
        mixer.music.play()
        print("["+time.strftime("%H:%M:%S",time.localtime())+"][Checkpoint 08] Speaking Answer: " + plain_answer.decode())
        time.sleep(5)


        s.close()



myStreamListener=MyStreamListener()
myStream=tweepy.Stream(auth = api.auth, listener = myStreamListener)
print("["+time.strftime("%H:%M:%S",time.localtime())+"][Checkpoint 02] Listening for tweets from Twitter API that contain questions")
data=myStream.filter(track=['#ECE4564T02'])







print ('Received:', plain_answer)
