from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response)
    return response.json()


@app.route("/")
def index():
    return render_template("index.html")


output = query({
    "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
})


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
