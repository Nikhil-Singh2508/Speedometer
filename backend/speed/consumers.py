import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import SpeedData

# UI Consumer
class SpeedConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "speed_group",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "speed_group",
            self.channel_name
        )

    async def send_speed(self, event):
        await self.send(text_data=json.dumps({
            "speed": event["speed"]
        }))


# Sensor Consumer
class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        speed = data.get("speed", 0)

        # store in DB 
        await sync_to_async(SpeedData.objects.create)(speed=speed)

        # broadcast to UI clients
        await self.channel_layer.group_send(
            "speed_group",
            {
                "type": "send_speed",
                "speed": speed
            }
        )
