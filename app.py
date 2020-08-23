from flask import Flask, render_template, request
import http.client
import urllib.request, urllib.parse, urllib.error
import json
import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

app = Flask(__name__)

# Twilio Initialization
load_dotenv()
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_KEY = os.getenv('TWILIO_KEY')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
client = Client(
    str(TWILIO_SID),
    str(TWILIO_KEY)
)

# FACE API
FACE_KEY = os.getenv('FACE_KEY')

# JOKES API
JOKES_API = os.getenv('JOKES_API')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    # Get FaceAttributes from Microsoft Face API
    subscription_key = FACE_KEY
    assert subscription_key

    face_api_url = 'https://spotifai.cognitiveservices.azure.com/face/v1.0/detect'

    image_url = str(request.args.get('url'))

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'returnFaceId': 'false',
        'returnFaceRectangle': 'false',
        'returnFaceAttributes': 'age,emotion',
    }

    response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
    age = response.json()[0]['faceAttributes']['age']
    emotion = response.json()[0]['faceAttributes']['emotion']['happiness']

    flags = ''
    if int(age) < 18:
        flags = '&blacklistFlags=nsfw%252Cracist%252Creligious%252Cpolitical%252Csexist'


    # Jokes API
    conn = http.client.HTTPSConnection("jokeapi-v2.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com",
        'x-rapidapi-key': JOKES_API
        }

    conn.request('GET', '/joke/Any?format=json' + str(flags) + '&idRange=0-150&type=single', headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    try:
        js = json.loads(data)
    except:
        js = None

    response = js['joke']

    # Sends the text message via the Twilio API, getting the phone number from the input and the joke from the Joke API
    number = request.args.get('phone').strip()
    msg = client.messages.create(
        to="+1" + str(number),
        from_=str(TWILIO_NUMBER),
        body=str(response),
    )

    print(f"Created a new message: {msg.sid}")

    return render_template('results.html', age=age, emotion=emotion, joke=response, image=image_url)
