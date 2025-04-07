from flask import Flask, render_template, request, jsonify
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re

app = Flask(__name__)

# Load the trained model and tokenizer
from huggingface_hub import snapshot_download

# Download model from Hugging Face Hub (only first time)
model_dir = snapshot_download(repo_id="abinash28/PurifyT5")

# Load from downloaded model directory
model = T5ForConditionalGeneration.from_pretrained(model_dir)
tokenizer = T5Tokenizer.from_pretrained(model_dir)


# Function to split text on punctuation
def split_sentences(text):
    # Split by punctuation that typically ends a sentence
    # This keeps the punctuation as part of the sentence
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return sentences

def replace_explicit_words(text):
    sentences = split_sentences(text)
    sanitized_sentences = []

    for sentence in sentences:
        if sentence.strip():  # skip empty strings
            input_ids = tokenizer.encode(sentence.strip(), return_tensors='pt')
            with torch.no_grad():
                output_ids = model.generate(input_ids, max_length=512, num_beams=5, early_stopping=True)
            sanitized = tokenizer.decode(output_ids[0], skip_special_tokens=True)
            sanitized_sentences.append(sanitized)
        else:
            sanitized_sentences.append("")  # maintain structure for any empty split

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




# from huggingface_hub import upload_folder

# upload_folder(
#     repo_id="abinash28/PurifyT5",  # replace this
#     folder_path="sanitizer_model",  # this is your folder
#     repo_type="model"
# )
