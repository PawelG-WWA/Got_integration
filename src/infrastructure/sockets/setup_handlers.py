from .sockets_setup import socketio
from flask import request
from openai import OpenAI

class Payload:
    def __init__(self, context, message):
        self.context = context
        self.message = message


def setup_socketio_handlers():
    @socketio.on("message")
    def handle_message(input):
        payload_data = Payload(**input['payload'])

        client = OpenAI()

        system_role = 'You are a helpful assistant'

        match payload_data.context:
            case 'Fitness':
                system_role = 'You are a goofy fitness trainer that keeps their pupils motivated'
            case 'CustomerAssistant':
                system_role = 'You are an assistant in a music school. You''re professional but also crazy a little about rock and heavy metal music. You speak in a typical heavy metal manner'

        response = client.chat.completions.create(
            model='gpt-4o',
            messages=[
                { 'role': 'system', 'content': system_role },
                { 'role': 'user', 'content': payload_data.message }
            ]
        )

        socketio.emit('response', {'data': response.choices[0].message.content}, room=request.sid)
    


