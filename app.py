from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)
YELP_API = os.getenv('YELP_KEY')
YELP_CLIENT = os.getenv('YELP_CLIENT')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    subscription_key = 'b2cf0902bf004b89b2a5096c2df5e0e3'
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
    emotion = response.json()[0]['faceAttributes']['emotion']
    return render_template('results.html', age=age, emotion=emotion)
