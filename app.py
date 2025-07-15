
# app.py

import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

from mcp import get_events
from models.gemini import query_gemini
from models.openai import query_openai
from models.llama import query_llama

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask/<model>", methods=["POST"])
def ask_model(model):
    data = request.json
    question = data.get("question")
    city = data.get("city")

    events = get_events(city)
    if events:
        context = f"Here are the events in {city}: " + ", ".join(
            f"{e['title']} on {e['date']} at {e['location']}" for e in events
        )
    else:
        context = f"No events found in {city}."

    final_prompt = f"Context:\n{context}\n\nUser question:\n{question}"

    try:
        if model == "gemini":
            answer = query_gemini(final_prompt)
        elif model == "openai":
            answer = query_openai(final_prompt)
        elif model == "llama":
            answer = query_llama(final_prompt)
        else:
            return jsonify({"error": "Unsupported model"}), 400

        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)