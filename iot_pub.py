"""
MQTT publisher line by line
Generate data "IoT sensors"
"""

import paho.mqtt.client as mqtt
import json
import time

# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "/data"


# Define on_publish event function
def on_publish(mqttc, userdata, mid):
    print("Message Published...")


def on_connect(mqttc, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # mqttc.subscribe(MQTT_TOPIC)
    # mqttc.publish(MQTT_TOPIC, MQTT_MSG)


# def on_message(mqttc, userdata, msg):
#     print(msg.topic)
#     print(msg.payload)  # <- do you mean this payload = {...} ?
#     # you can use json.loads to convert string to json
#     payload = json.loads(msg.payload)
#     print(payload)  # then you can check the value
#     mqttc.disconnect()  # Got message then disconnect

def on_log(client, userdata, level, buf):
    print("log: ", buf)

# Read JSON file
with open('data/sensors.json', 'r') as f:
    data = json.load(f)


# Initiate MQTT client
mqttc = mqtt.Client()

# Register callback functions
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
# mqttc.on_message = on_message
# mqttc.on_log = on_log

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Publish messege to MQTT Broker for each record in JSON file
for item in data:
    mqttc.publish(MQTT_TOPIC, json.dumps(item))
    time.sleep(10)

# Disconnect from MQTT Broker
mqttc.disconnect()
