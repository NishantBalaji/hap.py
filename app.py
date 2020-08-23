from flask import Flask, render_template, request
import http.client
import urllib
import json
import requests
import os
import dotenv

app = Flask(__name__)
YELP_API = os.getenv('YELP_KEY')
YELP_CLIENT = os.getenv('YELP_CLIENT')
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

    if



    return render_template('results.html', age=age, emotion=emotion)
