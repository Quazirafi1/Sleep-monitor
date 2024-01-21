import paho.mqtt.client as paho
import time
import random
import csv
from datetime import datetime
import pytz


def publishToMQTT(csv_file_path, on_publish_message, topic):

    broker = "172.30.0.110"
    port = 1883

    def on_publish(client, userdata, result):
        print(on_publish_message)
        pass

    client = paho.Client(topic)
    client.on_publish = on_publish
    # client.connect_async(broker, port)

    # Read and publish data from CSV
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader) 
            
            print(f"start trying publish for {topic}")

            for row in csv_reader:
                
                time.sleep(1)

                client.connect(broker, port)

                rome_tz = pytz.timezone('Europe/Rome')
                timestamp = datetime.now(rome_tz).strftime("%Y-%m-%d %H:%M:%S")

                data_map = {
                    "timestamp": timestamp,
                    "BloodOxygenLevel": row[0]
                }

                data_map_string = str(data_map)

                ret = client.publish(f"/SleepMonitor/{topic}", data_map_string.encode())
                client.disconnect()


    except IOError as e:
        print("An error occurred:", e)

    print(f"stopped publishing with {topic}")