# -*- coding: utf-8 -*-
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class WebConsumers(AsyncWebsocketConsumer):
    """处理通知应用的websocket请求"""

    async def connect(self):
        """建立连接"""
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        """断开连接"""
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        """接收到的消息，返回给前端"""
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': message}))
