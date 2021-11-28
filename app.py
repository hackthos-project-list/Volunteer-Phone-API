import json
import requests
import sys

from flask import Flask
from flask import request

if len( sys.argv ) < 4:
    print( 'Usage: python app.py SERVICE_URL API_USERNAME API_PASSWORD' )
    exit( 1 )

SERVICE_URL = sys.argv[1]
AUTH = ( sys.argv[2], sys.argv[3] )

GREETING_URL = "https://the-digital-volunteer.github.io/greeting.mp3"

app = Flask(__name__)

@app.route("/incomingCalls", methods=['POST'])
def home():
    print(request.form)
    response = {
        "play": GREETING_URL,
        "next": SERVICE_URL + "/beep"
    }
    return json.dumps(response)

@app.route("/beep", methods=['POST'])
def beep():
    print(request.form)
    response = {
        "play": "sound/beep",
        "next": SERVICE_URL + "/record"
    }
    return json.dumps(response)

@app.route("/record", methods=['POST'])
def record():
    print(request.form)
    response = {
        "record": SERVICE_URL + "/process"
    }
    return json.dumps(response)

@app.route("/process", methods=['POST'])
def process():
    print(request.form)

    recoverAudioFrom(request.form['wav'])

    return json.dumps({})

def recoverAudioFrom(url):
    fileName = url.split('/')[-1]

    with requests.get( url, auth=AUTH, stream=True ) as content:
        content.raise_for_status()

        with open( fileName, 'wb' ) as file:
            for chunk in content.iter_content( chunk_size=8192 ):
                if chunk:
                    file.write( chunk )

    return fileName

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5501)
