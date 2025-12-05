import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    lock1.acquire()
    print("Task1 acquired Lock1")
    time.sleep(1)
    lock2.acquire()
    print("Task1 acquired Lock2")
    lock2.release()
    lock1.release()

def task2():
    lock2.acquire()
    print("Task2 acquired Lock2")
    time.sleep(1)
    lock1.acquire()
    print("Task2 acquired Lock1")
    lock1.release()
    lock2.release()

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
print("Finished (may deadlock in some runs)")
Print("finished (may deadlock in some runs)") PY


