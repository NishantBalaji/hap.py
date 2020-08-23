from twilio.rest import Client
import os
import json
from dotenv import load_dotenv

load_dotenv()
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_KEY = os.getenv('TWILIO_KEY')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

client = Client(
    str(TWILIO_SID),
    str(TWILIO_KEY)
)

""" for msg in client.messages.list():
    print(msg.body)
     print(f"Deleting {msg.body}")
    msg.delete()"""

num = 19162208794
body = 'test'
msg = client.messages.create(
    to="+" + str(num),
    from_=str(TWILIO_NUMBER),
    body=str(body),
)

print(f"Created a new message: {msg.sid}")
