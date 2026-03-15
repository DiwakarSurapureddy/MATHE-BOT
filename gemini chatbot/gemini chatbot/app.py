from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os
from datetime import datetime

app = Flask(__name__)

genai.configure(api_key=" AIzaSyAlNhQozmiHqNlQw-FHZy09TKkf1ae_DwY")

# Use a supported model name for generate_content. "gemini-2.5-flash" is currently available.
model = genai.GenerativeModel("gemini-2.5-flash")

# History file path
HISTORY_PATH = "../../history.json"

def _load_history():
    """Load chat history from file"""
    if not os.path.exists(HISTORY_PATH):
        return {}
    try:
        with open(HISTORY_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}

def _save_history(history_data):
    """Save chat history to file"""
    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(history_data, f, ensure_ascii=True, indent=2)

# Load history on startup
chat_history = _load_history()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    data = request.json
    user_message = data.get("message", "")

    try:
        response = model.generate_content(user_message)
        bot_reply = response.text
        
        # Initialize messages list if not exists
        if "messages" not in chat_history:
            chat_history["messages"] = []
        
        # Add message pair to history
        chat_history["messages"].append({
            "user": user_message,
            "bot": bot_reply,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # Save history to file
        _save_history(chat_history)
        
        return jsonify({"reply": bot_reply})
    except Exception as e:
        # Log the error and return a JSON error response.
        app.logger.exception("Error generating response")
        return jsonify({"error": "Failed to generate response", "details": str(e)}), 500

@app.route("/history")
def get_history():
    """Get chat history"""
    return jsonify(chat_history.get("messages", []))

@app.route("/clear-history", methods=["POST"])
def clear_history():
    """Clear chat history"""
    global chat_history
    chat_history["messages"] = []
    _save_history(chat_history)
    return jsonify({"message": "History cleared"})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)