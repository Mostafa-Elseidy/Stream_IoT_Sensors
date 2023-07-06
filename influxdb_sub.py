"""
MQTT subscriber and store data to InfluxDB bucket
"""

import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time 
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/data")


def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    
    # Convert JSON data to line protocol and write to InfluxDB
    for key, value in json.loads(msg.payload.decode('utf-8')).items(): 
        if value is None:
            value = float(-999)
        point = Point(bucket).field(key, value)
        # print(point)
        write_api.write(bucket=bucket, record=point)
    # time.sleep(15)

    db_client.close()



def on_log(client, userdata, level, buf):
    print("log: ", buf)


# You can generate a Token from the "Tokens Tab" in the UI
token = "my-super-secret-token"
org = "myorg"
bucket = "sensor_data"

# Set up connection to InfluxDB
db_client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

# Find the bucket by its name
bucket_name = bucket
b = db_client.buckets_api().find_bucket_by_name(bucket_name)

# if b is not None:
#     # Get the bucket ID
#     bucket_id = b.id
#     # Delete the bucket
#     db_client.buckets_api().delete_bucket(bucket_id)
#     print("Old bucket deleted.")
#     # Create a bucket 
#     db_client.buckets_api().create_bucket(bucket_name=bucket, org_id=db_client.org)
#     print("new one created.")

# Check if the bucket was found
if b is None:
    print(f"Bucket '{bucket_name}' not found")
    # Create a bucket 
    db_client.buckets_api().create_bucket(bucket_name=bucket, org_id=db_client.org)
    print("new one created.")

write_api = db_client.write_api(write_options=SYNCHRONOUS)

db_client.close()

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
# mqtt_client.on_log = on_log

mqtt_client.connect("localhost", 1883, 60)

mqtt_client.loop_forever()


###########################################################################
##########################################################################
###########################################################################







