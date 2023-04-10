from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response)
    return response.json()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json["text"]
    data = {"text": text}
    response = requests.post(
        API_URL, headers=headers, data=json.dumps(data["text"]))
    output = response.json()
    print(output)
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
