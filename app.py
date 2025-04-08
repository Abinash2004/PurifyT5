from flask import Flask, render_template, request, jsonify
from gradio_client import Client
import re

app = Flask(__name__)

# Initialize Gradio client with your Hugging Face Space
client = Client("abinash28/PurifyT5")

# Function to split text on punctuation
def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return sentences

def replace_explicit_words(text):
    sentences = split_sentences(text)
    sanitized_sentences = []

    for sentence in sentences:
        if sentence.strip():
            try:
                # Call Gradio Space endpoint
                output = client.predict(
                    text=sentence.strip(),
                    api_name="/predict"
                )
                sanitized_sentences.append(output)
            except Exception as e:
                sanitized_sentences.append("[Error]")
        else:
            sanitized_sentences.append("")
    return ' '.join(sanitized_sentences)

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
