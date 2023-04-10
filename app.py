from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json

app = Flask(__name__)

API_URL = "http://20.96.47.248:5000/summarize"
CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json["text"]
    data = {"text": text}
    print(data)
    response = requests.post(
        API_URL, json=data)
    output = response.json()
    return (output)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
