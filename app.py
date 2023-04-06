from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)
CORS(app)

# Load the saved model and tokenizer
model_path = "./models/checkpoint-11250"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

max_input_length = 256
max_target_length = 50

# Define the root route to render the index.html file


@app.route("/")
def index():
    return render_template("index.html")


# Define the API route for summarization


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json["text"]
    inputs = tokenizer.encode(
        "summarize: " + text, return_tensors="pt", max_length=256, truncation=True)

    # Generate summary
    summary_ids = model.generate(
        inputs, num_beams=4, max_length=50, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
