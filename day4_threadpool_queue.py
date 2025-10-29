import threading
import queue
from concurrent.futures import ThreadPoolExecutor
import time
import random

def task(item):
    time.sleep(random.uniform(0.01, 0.1))
    print("Processed", item)
    return item * item

def main():
    q = queue.Queue(maxsize=50)
    with ThreadPoolExecutor(max_workers=4) as executor:
        def producer():
            for i in range(100):
                q.put(i)
            for _ in range(4):
                q.put(None)

        def consumer():
            while True:
                item = q.get()
                if item is None:
                    break
                future = executor.submit(task, item)
                result = future.result()
                print("Result:", result)
            print("Consumer done")

        t_prod = threading.Thread(target=producer)
        t_cons = threading.Thread(target=consumer)

        t_prod.start()
        t_cons.start()
        t_prod.join()
        t_cons.join()

if __name__ == "__main__":
    main()
