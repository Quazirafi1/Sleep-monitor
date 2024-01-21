#simulator device 1 for mqtt message publishing
import paho.mqtt.client as paho
import time
import random
import csv
from datetime import datetime
import pytz

import sys
sys.path.append('../Sleep-monitor')  # Adjust the path accordingly
import publisher

publisher.publishToMQTT('./HeartRate.csv', "Heart Rate Publisher : Data published.", 'HR')