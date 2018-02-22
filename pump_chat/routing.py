from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ChannelNameRouter, ProtocolTypeRouter
from django.urls import path
from chat import consumers

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/", consumers.CurseConsumer),
        ])
    ),
    "channel": ChannelNameRouter({
        "ws": consumers.CurseConsumer
    })
})

