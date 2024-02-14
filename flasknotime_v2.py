import threading
import time
import json
from datetime import datetime
import random

import paho.mqtt.client as mqtt

def connect_to_mqtt_server():
    mqtt_server = "test.mosquitto.org"
    mqtt_port = 1883
    device_id = "A"

    # Create an MQTT client instance
    client = mqtt.Client(device_id)

    # Connect to the MQTT broker
    client.connect(mqtt_server, mqtt_port)

    def task1():
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
        
            time.sleep(3)

    def task2():
        while True:
            # Your second task code goes here
            # ...
            
            time.sleep(5)

    # Create threads for each task
    thread_task1 = threading.Thread(target=task1)
    thread_task2 = threading.Thread(target=task2)

    # Start the threads
    thread_task1.start()
    thread_task2.start()

    # Wait for the threads to complete
    thread_task1.join()
    thread_task2.join()

# Call the function to connect to the MQTT server and run the tasks
connect_to_mqtt_server()
