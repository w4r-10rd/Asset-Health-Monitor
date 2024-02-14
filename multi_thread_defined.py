import threading
import time

def connect_to_mqtt_server():
    mqtt_server = "test.mosquitto.org"
    mqtt_port = 1883
    device_id = "A"

    # Your code to connect to the MQTT server goes here
    # ...

def task1():
    print("Task 1 started")
    time.sleep(3)  # Simulate some work
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(3)  # Simulate some work
    print("Task 2 completed")

# Create threads for each task
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

# Call the function to connect to the MQTT server
connect_to_mqtt_server()
