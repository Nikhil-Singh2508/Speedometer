from django.urls import path
from .consumers import SpeedConsumer, SensorConsumer

websocket_urlpatterns = [
    path("ws/speed/", SpeedConsumer.as_asgi()),   # UI
    path("ws/sensor/", SensorConsumer.as_asgi()), # Sensor
]
