# -*- coding: utf-8 -*-

from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from web.urls import websocket_url

# self.scope['type']获取协议类型
# self.scope['url_route']['kwargs']['username']获取url中关键字参数
# channels routing是scope级别的，一个连接只能由一个consumer接收和处理
application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        URLRouter(
            websocket_url
        )
    )
})