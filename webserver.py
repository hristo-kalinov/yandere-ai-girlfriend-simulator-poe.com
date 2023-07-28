from flask import Flask, request
import ssl
import poe
import logging
import sys
import time
import json
import poe
import logging
import sys
import time
import json
app = Flask(__name__)
TOKEN = "Your-poe.com-Token"
BOT = "chinchilla"
'''
  "capybara": "Assistant",
  "a2_100k": "Claude-instant-100k",
  "vizcacha": "GPT-4-32k",
  "chinchilla": "ChatGPT",
  "a2": "Claude-instant",
  "a2_2": "Claude-2-100k",
  "beaver": "GPT-4",
  "acouchy": "Google-PaLM",
  "agouti": "ChatGPT-16k",
  "llama_2_70b_chat": "Llama-2-70b"
'''
poe.logger.setLevel(logging.INFO)
client = poe.Client(token)
client.send_chat_break(bot)
@app.route('/v1/chat/completions', methods=['POST'])
def index():
    content = request.get_data().decode('utf-8')
    data = json.loads(content)
    api_message_content = ""
    if len(data["messages"])==2:
        client.send_chat_break(bot)
        api_message_content = data["messages"][-2]["content"] + "\n\n\nSenpai's first message: " + data["messages"][-1]["content"]
    else:
        api_message_content = data["messages"][-1]["content"]
    print(api_message_content)
    for chunk in client.send_message(bot, api_message_content):
        pass
    response = chunk["text"]
    print(response)
    data = {
            "choices": [
                {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": response,
                    "role": "system"
                }
                }
            ],
            "created": 1677664795,
            "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
            "model": "gpt-3.5-turbo-0613",
            "object": "chat.completion",
            "usage": {
                "completion_tokens": 17,
                "prompt_tokens": 57,
                "total_tokens": 74
            }
        }
    return data

if __name__ == '__main__':
    certfile = 'certificate.pem'  # Path to your self-signed certificate file
    keyfile = 'private_key.pem'   # Path to your private key file
    server_address = ('0.0.0.0', 443)  # Bind to all available network interfaces on port 443

    # Create an SSL context with the specified certificate and private key files
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)

    # Run the Flask app with the HTTPS server and SSL context
    app.run(host=server_address[0], port=server_address[1], ssl_context=ssl_context)