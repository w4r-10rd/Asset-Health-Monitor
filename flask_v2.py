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

    client = mqtt.Client(device_id)
    client.connect(mqtt_server, mqtt_port)

    def task1():
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            data = {
                "{}".format(device_id) : {
                    "Timestamp": timestamp,
                    "Temperature": int((random.uniform(0, 5) - 0.5) * 10),
                    "Ultrasonic": int(round(random.uniform(1, 5) + random.uniform(0, 5), 2)),
                    
                    "Vibration_X": round(random.uniform(2, 6) + random.uniform(0, 5), 2),
                    "Vibration_Y": round(random.uniform(3, 9) + random.uniform(0, 5), 2),
                    "Vibration_Z": round(random.uniform(4, 16) + random.uniform(0, 5), 2),
                    
                    "EMF_X": round(random.uniform(0, 5), 2),
                    "EMF_Y": round(random.uniform(0, 5), 2),
                    "EMF_Z": round(random.uniform(0, 5), 2)
                }
            }
        
            data_json = json.dumps(data)
            
           
            client.publish("test_1", data_json)
        
            print("Published data: {}".format(data_json))
        
            time.sleep(3)

    def task2():
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            data = {
                "{}".format(device_id) : {
                    "Timestamp": timestamp,
                    "Temperature": int((random.uniform(0, 5) - 0.5) * 10),
                    "Ultrasonic": int(round(random.uniform(1, 5) + random.uniform(0, 5), 2)),
                    
                    "Vibration_X": round(random.uniform(2, 6) + random.uniform(0, 5), 2),
                    "Vibration_Y": round(random.uniform(3, 9) + random.uniform(0, 5), 2), 
                    "Vibration_Z": round(random.uniform(4, 16) + random.uniform(0, 5), 2),
                    
                    "EMF_X": round(random.uniform(0, 5), 2),
                    "EMF_Y": round(random.uniform(0, 5), 2),
                    "EMF_Z": round(random.uniform(0, 5), 2) 
                }
            }
        
            data_json = json.dumps(data)
            
            
            client.publish("test_1", data_json)
        
            print("Published data: {}".format(data_json))
        
            time.sleep(5)

    
    thread_task1 = threading.Thread(target=task1)
    thread_task2 = threading.Thread(target=task2)

   
    thread_task1.start()
    thread_task2.start()

   
    thread_task1.join()
    thread_task2.join()

connect_to_mqtt_server()
