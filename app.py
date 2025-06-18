from flask import Flask, request, jsonify
import openai
import os
import json

app = Flask(__name__)

# ✅ Load keys
openai.api_key = os.getenv("OPENAI_API_KEY")
memory_file = os.getenv("MEMORY_FILE", "memory.json")

# ✅ Load memory
if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        memory = json.load(f)
else:
    memory = []

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    user_input = data.get("text", "")

    memory.append({"user": user_input})
    if len(memory) > 10:
        memory.pop(0)

    # ✅ ChatGPT Response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Tamil-English kind assistant named Akku."},
            {"role": "user", "content": user_input}
        ]
    )
    reply = response['choices'][0]['message']['content'].strip()
    memory.append({"ai": reply})

    # Save memory
    with open(memory_file, "w") as f:
        json.dump(memory, f)

    return jsonify({"reply": reply})

# ✅ Fix for Render Deployment

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
