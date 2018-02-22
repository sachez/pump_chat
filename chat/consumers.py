from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .helpers import get_curse
import json


class CurseConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)("curse", self.channel_name)
        self.send(json.dumps(get_curse()))

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_send)(
            "curse",
            {
                "type": "curse.send",
                "text": text_data['text']
             }
        )

    def curse_send(self, event):
        self.send(text_data=event['text'])

    def disconnect(self, close_code):
        # Called when the socket closes
        super().disconnect(404)

class ChatConsumer(WebsocketConsumer):
    pass


