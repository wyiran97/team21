#!/usr/bin/env python3

"""
A simple echo client
"""
import tweepy
import socket
import Key
from cryptography.fernet import Fernet
import hashlib

host = '192.168.8.235'
port = 50000
size = 1024
#auth
auth=tweepy.OAuthHandler(Key.APIkey,Key.APISkey)
auth.set_access_token(Key.Accesstoken,Key.AccessStoken)
api=tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
     def on_status(self,status):
        print(status.text)
        str_text=status.text
        #exclude hash tag
        str_text=str_text.replace("@ECE4564T02","")
        #cipher_key
        cipher_key = Fernet.generate_key()
        cipher = Fernet(cipher_key)
        print(cipher_key)
        #transfer text from str to byte
        byte_text = bytes(str_text,encoding="utf8")
        print(byte_text)
        #encrypt text
        en_text = cipher.encrypt(byte_text)
        # hash of text
        md=hashlib.md5()
        md.update(byte_text)
        hash_text = md.hexdigest
        print(hash_text)
        #s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect((host,port))
        #s.send(status.text.encode("utf-8"))
        #data=s.recv(size)
        #s.close()
				



myStreamListener=MyStreamListener()
myStream=tweepy.Stream(auth = api.auth, listener = myStreamListener)
data=myStream.filter(track=['#ECE4564T02'])




#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host,port))

#s.send(b'Hello, world')
#data = s.recv(size)
#s.close()
#print ('Received:', data)
