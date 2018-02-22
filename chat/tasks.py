from celery import shared_task
import json
from asgiref.sync import async_to_sync
from .helpers import get_curse
from channels.layers import get_channel_layer

@shared_task
def sent_curse():
    channel_layer = get_channel_layer()
#    json_str_curse = json.dumps(get_curse())

    async_to_sync(channel_layer.group_send)("curse", message={
        "type": "receive",
        "text": json.dumps(get_curse())
    })

