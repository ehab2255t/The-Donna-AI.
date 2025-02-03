from flask import Flask, request, jsonify
from chatbot import get_response
from voice import synthesize_speech

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    response = get_response(user_input)
    return jsonify({"response": response})

@app.route('/voice', methods=['POST'])
def voice():
    text = request.json.get("text", "")
    audio_file = synthesize_speech(text)
    return jsonify({"audio": audio_file})

if __name__ == '__main__':
    app.run(debug=True)
