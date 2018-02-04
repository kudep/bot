
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
from settings import *
# import messageHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = 'Hello from Flask!'
    print(response)
    return response

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        response = 'not vk'
        print(response)
        return response
    if data['type'] == 'confirmation':
        response = confirmation_token
        print(response)
        return response
    elif data['type'] == 'message_new':
        # messageHandler.create_answer(data['object'], token)
        response = 'ok'
        print(response)
        return response
