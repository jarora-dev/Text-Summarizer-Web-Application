import os
import json
from transformers import T5ForConditionalGeneration, T5Tokenizer

model = None
tokenizer = None


def init():
    global model, tokenizer
    model_path = "./checkpoint-11250"
    tokenizer = T5Tokenizer.from_pretrained(model_path)
    model = T5ForConditionalGeneration.from_pretrained(model_path)


def run(raw_data):
    global model, tokenizer
    max_input_length = 256
    max_target_length = 50

    data = json.loads(raw_data)
    text = data["text"]
    inputs = tokenizer.encode(
        "summarize: " + text, return_tensors="pt", max_length=256, truncation=True
    )

    summary_ids = model.generate(
        inputs, num_beams=4, max_length=50, early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return json.dumps({"summary": summary})
