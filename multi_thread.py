import concurrent.futures
import time

def task1():
    print("Task 1 started")
    time.sleep(3)  # Simulate some work
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(3)  # Simulate some work
    print("Task 2 completed")

# Create a ThreadPoolExecutor with 2 worker threads
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

# Submit the tasks to the executor
future1 = executor.submit(task1)
future2 = executor.submit(task2)

# Wait for the tasks to complete
concurrent.futures.wait([future1, future2])
