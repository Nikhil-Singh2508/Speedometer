import websocket
import json
import time
import random

try:
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8000/ws/sensor/")
except Exception as e:
    print("Connection error:", e)
    exit(1)

while True:
    try:
        speed = random.randint(0, 120)
        ws.send(json.dumps({"speed": speed}))
        print("Sent:", speed)
        time.sleep(1)
    except Exception as e:
        print("Error:", e)
        break