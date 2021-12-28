#SEND SMS TWILIO
from twilio.rest import Client
# import variables from credentials.py
from credentials import account_sid, auth_token, my_cell, my_twilio
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 17:24:35 2021
Send SMS Using Twilio API
@author: yousuf
"""


client = Client(account_sid, auth_token)

# send text to my_cell from twilio number
my_msg = ''.join(['Silly bob\n' for i in range(100)])

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)

