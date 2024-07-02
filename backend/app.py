from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)
load_dotenv()


client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages', [])
    api_messages = [{'role': 'user', 'content': msg['content']} for msg in messages]
    system_message = {'role': 'system', 'content': 'Speak like a travel Agent'}
    api_messages.insert(0, system_message)

    try:
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages= api_messages
        )
        chat_gpt_message=response.choices[0].message.content

        response_message = {
            'role': 'assistant',
            'content': chat_gpt_message
        }

        messages.append(response_message)
        return jsonify(messages), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)
