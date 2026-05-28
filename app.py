from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os
import random
from datetime import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

genai.configure(api_key=" AIzaSyAlNhQozmiHqNlQw-FHZy09TKkf1ae_DwY")

# Use a supported model name for generate_content
model = genai.GenerativeModel("gemini-2.5-flash")

# History file path
HISTORY_PATH = "history.json"

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
    return render_template("home.html")

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    data = request.json
    user_message = data.get("message", "")

    system_prompt = """You are SolveMate AI, a mathematics expert.
IMPORTANT: Format your responses EXACTLY like this for every math problem:

STEP 1: [First step description]
Calculation: [show the calculation]
Result: [the result]

STEP 2: [Second step description]
Calculation: [show the calculation]
Result: [the result]

STEP 3: [Third step description]
Calculation: [show the calculation]
Result: [the result]

Continue with more steps if needed...

FINAL ANSWER: [Only the final numerical answer, no symbols]

RULES:
- Use one step per block
- Show all calculations clearly
- Use proper mathematical notation
- For trigonometry (sin, cos, tan): show angle conversions and values
- Number each step sequentially
- Make it crystal clear and easy to follow
- No dollar signs, no LaTeX formatting in final answer"""

    try:
        response = model.generate_content(f"{system_prompt}\n\nProblem: {user_message}")
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
        app.logger.exception("Error generating response")
        return jsonify({"error": "Failed to generate response", "details": str(e)}), 500

@app.route("/history")
def get_history():
    """Get chat history"""
    return jsonify(chat_history.get("messages", []))

@app.route("/delete-history/<int:index>", methods=["DELETE"])
def delete_history_item(index):
    """Delete a specific chat history item"""
    global chat_history
    messages = chat_history.get("messages", [])
    if 0 <= index < len(messages):
        messages.pop(index)
        _save_history(chat_history)
        return jsonify({"message": "History item deleted"})
    return jsonify({"error": "Invalid index"}), 400

@app.route("/clear-history", methods=["POST"])
def clear_history():
    """Clear chat history"""
    global chat_history
    chat_history["messages"] = []
    _save_history(chat_history)
    return jsonify({"message": "History cleared"})

@app.route("/suggest", methods=["GET"])
def suggest():
    """Provide random math problem suggestion"""
    suggestions = [
        "Solve for x: 3x + 7 = 22",
        "Calculate: sin(45°) + cos(45°)",
        "Integrate: ∫ 2x dx from 0 to 5",
        "Find the derivative of f(x) = x³ + 2x² - x + 1",
        "Solve: 2.5 × 9 + 9(88 - 0) + 2",
        "What is tan(60°)?",
        "Calculate: (5 + 3)² - √16",
        "Find the limit: lim(x→2) x² + 3x - 2",
        "Solve the quadratic: x² - 5x + 6 = 0",
        "Calculate: e^(iπ) + 1",
        "What is arcsin(0.5)?",
        "Integrate: ∫ e^x dx",
        "Solve: |2x - 3| = 7",
        "Find the area under y = x² from 0 to 3",
        "Calculate: log₁₀(100) + ln(e)"
    ]
    return jsonify({"suggestion": random.choice(suggestions)})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

