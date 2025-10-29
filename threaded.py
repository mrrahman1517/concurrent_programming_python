"""
Multi-threaded CPU-bound Program - Demonstrating GIL Limitations

This program demonstrates why multi-threading does NOT improve performance
for CPU-bound tasks in Python due to the Global Interpreter Lock (GIL).

The GIL allows only one thread to execute Python bytecode at a time,
effectively serializing CPU-intensive operations across multiple threads.

Key Observations:
- Adding more threads provides NO speedup for CPU-bound work
- May introduce slight overhead due to thread creation and context switching
- All threads run sequentially, not in parallel
- This is a fundamental limitation of CPython's threading model

Expected Results:
- 1 thread: ~0.67 seconds (baseline)
- 2 threads: ~0.67 seconds (no improvement)
- 4 threads: ~0.67 seconds (no improvement)
- 8 threads: ~0.68 seconds (slight overhead)

Alternatives for CPU-bound parallelism:
- multiprocessing: Use separate processes (no GIL sharing)
- NumPy/Cython: C extensions that can release the GIL
- PyPy: JIT compiler with better threading performance
"""

import threading
import time

def countdown(n):
    """
    Same CPU-intensive countdown function as in seq.py.
    
    This function will be executed by multiple threads,
    but due to the GIL, only one thread can execute
    Python bytecode at a time.
    
    Args:
        n (int): Starting number to countdown from
    """
    while n > 0:
        n -= 1

# Same workload as sequential version for fair comparison
COUNT = 50000000

print("Multi-threaded version with GIL impact:")
print("=" * 50)

# Test with different numbers of threads to show GIL impact
# We expect no performance improvement, demonstrating GIL limitations
thread_counts = [1, 2, 4, 8]

for num_threads in thread_counts:
    start = time.time()
    threads = []
    
    # Create and start threads
    # Each thread gets an equal portion of the total work
    for i in range(num_threads):
        t = threading.Thread(target=countdown, args=(COUNT//num_threads,))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    # This ensures we measure total execution time
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

print("\nConclusion:")
print("Threading provides NO benefit for CPU-bound tasks due to the GIL!")
print("For CPU parallelism, use multiprocessing instead.")