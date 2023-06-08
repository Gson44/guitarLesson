from flask import Flask, jsonify
from flask_cors import CORS

application = Flask(__name__)
CORS(application)
data ={"results": [
      {
        "name": "Chord C",
        "url": 
"https://drive.google.com/file/d/1O5PljPDKt20UtEtmr2JP4LmAiFRa_9IE/view?usp=drive_link"
      },
      {
        "name": "Chord D",
        "url": "Do something"
      }
    ]}

@application.route("/")
def hello():
    return jsonify(data)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080)

