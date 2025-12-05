import threading
import time

def worker():
    print("Worker thread starting")
    time.sleep(1)
    print("Worker thread ending")

t = threading.Thread(target=worker)
t.start()
t.join()

print("Main thread finished")
