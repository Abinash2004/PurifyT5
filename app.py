from flask import Flask, render_template, request, jsonify
from gradio_client import Client
import re

app = Flask(__name__)

# Initialize Gradio client with your Hugging Face Space
client = Client("abinash28/PurifyT5")


def replace_explicit_words(text):
    output = client.predict(text=text,api_name="/predict")
    return output

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sanitize', methods=['POST'])
def sanitize_text():
    data = request.json
    input_text = data.get("text", "")
    sanitized_text = replace_explicit_words(input_text)
    return jsonify({"sanitized_text": sanitized_text})

if __name__ == '__main__':
    app.run(debug=True)
