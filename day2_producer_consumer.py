import threading
import queue
import time
import random

q = queue.Queue(maxsize=10)
stop_sentinel = object()

def producer(num_items):
    for i in range(num_items):
        item = f"item-{i}"
        q.put(item)
        print("Produced", item)
        time.sleep(random.uniform(0.01, 0.1))
    q.put(stop_sentinel)

def consumer():
    while True:
        item = q.get()
        if item is stop_sentinel:
            break
        print("Consumed", item)
        q.task_done()
    print("Consumer done")

prod = threading.Thread(target=producer, args=(20,))
cons = threading.Thread(target=consumer)

prod.start()
cons.start()
prod.join()
cons.join()
