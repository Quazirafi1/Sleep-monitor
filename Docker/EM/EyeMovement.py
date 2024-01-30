#simulator device 1 for mqtt message publishing
import paho.mqtt.client as paho
import time
import random
import csv
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

load_dotenv()

print('starting simulation')

# hostname
broker = os.environ.get('MQTT_IP')
port = int(os.environ.get('MQTT_PORT'))

def on_publish(client, userdata, result):
    print("Eye Movement Publisher : Data published.")
    pass

print('connecting to mosquitto')

client = paho.Client("EM_client")
client.on_publish = on_publish
client.connect(broker, port)
client.loop_start()

print ('connected to mqtt')

# Path to the CSV file
csv_file_path = './EyeMovement.csv'
delimiter = ','
data_map = {}

# Read and publish data from CSV
try:
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if there is one
        for row in csv_reader:
            # message = f"Device 1 : Data {','.join(row)}"
            # ret = client.publish("/xyz", message)
            time.sleep(random.randint(1, 5))  # Random delay between 1 and 5 seconds

            rome_tz = pytz.timezone('Europe/Rome')
            timestamp = datetime.now(rome_tz).strftime("%Y-%m-%d %H:%M:%S")

            data_map = {
                "timestamp": timestamp,
                "EyeMovement": row[0]
            }

            data_map_string = str(data_map)
            # message = mqtt.MqttMessage()
            # message.payload = data_map_string.encode()
            
            # message = f"Device 1 : Data {','.join(row)}"
            ret = client.publish("/SleepMonitor/EM", data_map_string.encode())
            print(ret.rc)
            try:
                ret.wait_for_publish()
            except RuntimeError as e:
                print(e)
                client.connect(broker, port)

            print('data published')
            
            time.sleep(5) 

except IOError as e:
    print("An error occurred:", e)

print("stopped")

client.loop_stop()
