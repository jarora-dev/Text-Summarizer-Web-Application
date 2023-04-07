from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

# Replace <your_azure_endpoint> with your actual Azure endpoint
azure_endpoint = "https://text-summarizer.eastus2.inference.ml.azure.com/score"
# Replace <your_azure_key> with your actual Azure key
azure_key = "test"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {azure_key}",
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json["text"]
    data = {"text": text}
    response = requests.post(
        azure_endpoint, headers=headers, data=json.dumps(data))
    summary = response.json()
    return jsonify(summary)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
