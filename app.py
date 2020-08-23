from flask import Flask, render_template, request
from twilio.rest import Client
import http.client
import urllib.request, urllib.parse, urllib.error
import json
import requests
import os
import praw
from dotenv import load_dotenv

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


reddit = praw.Reddit(client_id="my client id",
                     client_secret="my client secret",
                     user_agent="my user agent")


FACE_KEY = os.getenv('FACE_KEY')

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
        flags = '?blacklistFlags=nsfw,religious,political,racist,sexist'

    if int(emotion) == 1:
        joke_count = 1
        count_param = ''
    else:
        joke_count = str((1 - int(emotion)) * 10)
        count_param = f'&amount={joke_count}'


    # Jokes API
    conn = http.client.HTTPSConnection('sv443.net')
    conn.request("GET", "/jokeapi/v2/joke/Any/" + str(flags) + '&type=single' + str(count_param))

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    js = json.loads(data)
    print(js)

    """try:
        js = json.loads(data)
    except:
        js = None"""

    if joke_count == 1:
        response = js["joke"]
    else:
        for joke in js["jokes"][0]:
            response = response + joke["joke"] + '\n'

    return render_template('results.html', age=age, emotion=emotion, joke=response, image=image_url)

    # Send the text to the phone, by getting the destination phone number and the joke
    msg = client.messages.create(
        to="+" + str(request.args.get('phone')).strip(),
        from_=str(TWILIO_NUMBER),
        body=str(response),
    )
