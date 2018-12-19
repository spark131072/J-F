from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
<<<<<<< HEAD

ASGI_APPLICATION = "helloworld.routing.application"
=======
>>>>>>> 44e95f6776cffdb2b004a9832151f3b8234bff17
