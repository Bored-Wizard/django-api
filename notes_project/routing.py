from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddleware
import notes.routing

application = ProtocolTypeRouter({
    "websocket": AuthMiddleware(
        URLRouter(
            notes.routing.websocket_urlpatterns
        )
    )
})