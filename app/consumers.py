from channels.consumer import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import User, ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        print(self.user)
        if not self.user.is_authenticated:
            await self.close()
            return
        await self.channel_layer.group_add(f"user_{self.user.id}", self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            f"user_{self.user.id}", self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")
        receiver_id = data.get("receiver_id")

        if message and receiver_id:
            await self.save_message(message, receiver_id)

            await self.channel_layer.group_send(
                f"user_{receiver_id}",
                {
                    "type": "chat_message",
                    "message": message,
                    "sender_id": self.user.id,
                },
            )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps(
                {"message": event["message"], "sender_id": event["sender_id"]}
            )
        )

    @database_sync_to_async
    def save_message(self, message, receiver_id):
        receiver = User.objects.get(id=receiver_id)
        ChatMessage.objects.create(sender=self.user, receiver=receiver, content=message)
