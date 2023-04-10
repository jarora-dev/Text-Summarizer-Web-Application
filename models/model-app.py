from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import logging
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
model_path = "./checkpoint-11250"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json["text"]
    logger.info(f"Received text: {text}")
    inputs = tokenizer.encode(
        "summarize: " + text, return_tensors="pt", max_length=256, truncation=True
    )
    summary_ids = model.generate(
        inputs, num_beams=4, max_length=50, early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
