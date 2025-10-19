import threading
import time

def countdown(n):
    while n > 0:
        n -= 1

COUNT = 50000000

print("Multi-threaded version with GIL impact:")
print("=" * 50)

# Test with different numbers of threads
thread_counts = [1, 2, 4, 8]

for num_threads in thread_counts:
    start = time.time()
    threads = []
    
    # Create and start threads
    for i in range(num_threads):
        t = threading.Thread(target=countdown, args=(COUNT//num_threads,))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    end = time.time()
    duration = end - start
    
    print(f"{num_threads} thread(s): {duration:.4f} seconds")

print("\nFor comparison, single-threaded sequential version:")
start = time.time()
countdown(COUNT)
end = time.time()
print(f"Sequential: {end - start:.4f} seconds")