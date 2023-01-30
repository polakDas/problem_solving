import threading
import time

def print_numbers(num):
    for i in range(1, num + 1):
        print("Searching........")
        time.sleep(1)

# create a thread
thread = threading.Thread(target=print_numbers, args=[100,])

# start the thread
thread.start()

# wait for the thread to finish
print("Waiting the the thread to finish.")
thread.join()
print("The end.")