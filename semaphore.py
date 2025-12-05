import threading
import time

sema = threading.Semaphore(2)

def worker(id):
    sema.acquire()
    print(f"Worker {id} entered")
    time.sleep(1)
    print(f"Worker {id} leaving")
    sema.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("All workers finished")
PY 

