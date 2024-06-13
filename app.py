from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# In-memory storage for chat messages (not suitable for production)
messages = []

@app.route('/chat')
def index():
    return render_template('chat.html')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/chats')
def chats():
    return render_template('chats.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    if message:
        messages.append(message)
        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/get_messages')
def get_messages():
    return jsonify(messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
