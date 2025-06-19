# 🧼 PurifyT5 – AI-Powered Text Sanitization Web App

Ever wanted your text to behave? **PurifyT5** is a smart web app that uses a fine-tuned **T5 transformer** to clean up toxic, explicit, or inappropriate content from user-generated input — making it safer for public use, moderation systems, or even your grandma.

🚀 Live Demo: [https://mild-shoshanna-abinashparida-5307eebe.koyeb.app/](https://mild-shoshanna-abinashparida-5307eebe.koyeb.app/)

---

## ✨ What It Does

- 🧠 Uses a fine-tuned **T5 transformer model** to detect and sanitize offensive or NSFW text
- 🔄 Real-time inference with Flask backend and Hugging Face model
- 💬 Input → Cleaned Output in under 25 seconds (usually way faster unless your WiFi is chewing gum)
- 🧪 Preprocessed with NLTK, regex, and lemmatization to improve model accuracy
- 🚫 Designed for chatbots, forms, forums, and any text submission where moderation is needed

---

## 🛠 Tech Stack

🧠 **Model:** T5 Transformer (fine-tuned on explicit comment dataset)  
🐍 **Backend:** Python, Flask  
⚙️ **ML Frameworks:** PyTorch, Hugging Face Transformers  
🧹 **Text Processing:** NLTK, Regex, Lemmatization  
🌐 **APIs:** RESTful endpoints for real-time sanitization  
🚀 **Deployment:** Koyeb (fast, free, and serverless)

---

## ⚙️ How It Works

1. ✍️ User inputs any text (PG-rated or not, we’re not judging).
2. 🧪 The model identifies toxic/explicit content.
3. 🧼 The sanitized version is returned — safer, cleaner, and ready for public eyes.
4. ⚡ All in ~1–3 seconds depending on server cold start & input length.

---

## 💻 Local Setup

Wanna run this locally? Here's the sanitization spellbook:

```bash
# 1. Clone the repo
git clone https://github.com/Abinash2004/PurifyT5.git
cd PurifyT5

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # (Use venv\Scripts\activate on Windows)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask server
python app.py
