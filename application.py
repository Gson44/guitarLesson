from flask import Flask, jsonify
application = Flask(__name__)

data ={"results": [
      {
        "name": "Chord C",
        "url": "something"
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

