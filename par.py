"""
Parallel CPU-bound Program - Threading Performance Test

This program demonstrates why threading doesn't improve performance
for CPU-bound tasks in Python due to the Global Interpreter Lock (GIL).

The work is split between two threads, each handling 25 million decrements.
Despite using multiple threads, the GIL ensures only one thread executes
Python bytecode at a time, resulting in no performance improvement.

Key Characteristics:
- CPU-bound: Pure computational work (no I/O)
- Multi-threaded: Uses two threads for parallel work attempt
- GIL-limited: Performance constrained by Global Interpreter Lock

Expected Performance:
- Should take approximately the same time as seq.py (~0.66s)
- No speedup despite using 2 threads
- May even be slightly slower due to threading overhead

This demonstrates the fundamental limitation of Python threading
for CPU-intensive tasks.
"""

from threading import Thread
import time 

def countdown(n):
    """
    Perform a simple countdown operation.
    
    This function represents CPU-intensive work by decrementing
    a counter in a tight loop. When run in multiple threads,
    the GIL prevents true parallel execution.
    
    Args:
        n (int): Starting number to countdown from
        
    Returns:
        None: Function completes when n reaches 0
    """
    while n > 0:
        n -= 1

# Configuration: 50 million iterations split between 2 threads
# Each thread handles 25 million iterations
COUNT = 50000000

# Create two threads, each handling half the work
t1 = Thread(target=countdown, name="thread1", args=(COUNT//2,))
t2 = Thread(target=countdown, name="thread2", args=(COUNT//2,))

# Start timing
start = time.time()

# Start both threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

# End timing
end = time.time()

# Display results
execution_time = end - start
print(f"Parallel execution time (2 threads): {execution_time:.4f} seconds")
print(f"Operations per second: {COUNT/execution_time:,.0f}")
print(f"Thread overhead vs sequential: {((execution_time/0.66) - 1) * 100:+.1f}%")
print("\nObservation: No speedup due to Python's GIL!")
print("For CPU-bound tasks, threading adds overhead without benefits.")
