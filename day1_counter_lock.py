import threading

counter = 0
lock = threading.Lock()

def worker(n):
    global counter
    for _ in range(n):
        lock.acquire()
        try:
            counter += 1
        finally:
            lock.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(100000,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final counter:", counter)
