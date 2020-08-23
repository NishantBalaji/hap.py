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

msg = client.messages.create(
    to="+19162208794",
    from_=str(TWILIO_NUMBER),
    body="Hello from Python",
)

print(f"Created a new message: {msg.sid}")
