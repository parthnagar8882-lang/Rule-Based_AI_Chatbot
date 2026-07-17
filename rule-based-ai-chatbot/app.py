"""Flask routes for the Rule-Based AI Chatbot."""

from flask import Flask, jsonify, render_template, request

from chatbot import get_response


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/chat")
def chat():
    """Receive one JSON message and return the matching predefined response."""
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or "message" not in data:
        return jsonify({"response": "Please send a valid message.", "is_exit": False}), 400

    if not isinstance(data["message"], str):
        return jsonify({"response": "Please send your message as text.", "is_exit": False}), 400

    try:
        response, is_exit = get_response(data["message"])
        return jsonify({"response": response, "is_exit": is_exit})
    except Exception:
        return jsonify({"response": "Sorry, something went wrong. Please try again.", "is_exit": False}), 500


if __name__ == "__main__":
    app.run(debug=True)
