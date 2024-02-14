import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from datetime import datetime
import paho.mqtt.client as mqtt
import json
import requests
import random
from flask import Flask, request, jsonify


# Define the MQTT server address and port
mqtt_server = "test.mosquitto.org"
mqtt_port = 1883
device_id = "A"


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create two instances of the ADS1115 class with different I2C addresses
ads0 = ADS.ADS1115(i2c, address=0x48)
ads1 = ADS.ADS1115(i2c, address=0x49)

# Create analog input objects for each channel on both ADS1115 modules
chan0 = AnalogIn(ads0, ADS.P0)
chan1 = AnalogIn(ads0, ADS.P1)
chan2 = AnalogIn(ads0, ADS.P2)
chan3 = AnalogIn(ads0, ADS.P3)
chan4 = AnalogIn(ads1, ADS.P0)
chan5 = AnalogIn(ads1, ADS.P1)
chan6 = AnalogIn(ads1, ADS.P2)
chan7 = AnalogIn(ads1, ADS.P3)

# Flask server
# app = Flask(__name__)

# @app.route('/data', methods=['POST'])
#def receive_data():
    #data = request.get_json()
    #print("Received data: {}".format(data))
    #return jsonify(success=True)

# mqtt client
client = mqtt.Client("TEST-MQTT-DEVICE")

# Connect to the MQTT broker
client.connect(mqtt_server, mqtt_port)


# Read and publish analog values from each channel
while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data = {
    "{}".format(device_id) : {
    
        "Timestamp": timestamp,
        "Temperature": int((chan0.voltage - 0.5) * 10), # Temperature Value
        "Ultrasonic": int(round(random.uniform(1, 5), 2)) + int(chan1.voltage), # Ultrasonic
        
        "Vibration_X": round( int(round(random.uniform(2, 4), 2)) + chan2.voltage, 2 ), # Vibration X
        "Vibration_Y": round( int(round(random.uniform(3, 6), 2)) + chan3.voltage, 2 ), # Vibration Y
        "Vibration_Z": round( int(round(random.uniform(4, 8), 2)) + chan4.voltage, 2 ), # Vibration Z
        
        "EMF_X": round(chan5.voltage, 2), # EMF X
        "EMF_Y": round(chan6.voltage, 2), # EMF Y
        "EMF_Z": round(chan7.voltage, 2)  # EMF Z
    }
    }

    data_json = json.dumps(data)
    
    # Publish the data to the MQTT broker
    client.publish("test_1", data_json)

    print("Published data: {}".format(data_json))

    time.sleep(5)
