import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import (MessagingResponse, Message, Body, Media)
#  Get a  SMS request, Parse and serach for time , based on time, respond with Good Morning or  Good adternoon
app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
      
      body = request.values.get('Body', None)
      fromCity = request.values.get('FromCity', None)
      fromZip   = request.values.get('FromZip', None)
      # print  body
      resp2 = MessagingResponse()
      if body=='h':
         resp2.message("Hello ")
         resp2.message(fromCity)
         resp2.message(fromZip)
         print(resp2.message)   
      elif body=='b':
         resp2.msg("goodbye")     
      return str(resp2)

if __name__ == "__main__":
       app.run(debug=True)
