"""
Sequential CPU-bound Program - Baseline Performance Test

This program demonstrates a simple CPU-intensive task that performs
50 million decrements in a tight loop. It serves as a baseline for
comparing single-threaded vs multi-threaded performance.

Key Characteristics:
- CPU-bound: Pure computational work (no I/O)
- Single-threaded: Uses only one thread of execution
- GIL-friendly: No threading overhead since only one thread is used

Performance Notes:
- On modern hardware (Apple M3 Pro), this runs in ~0.66 seconds
- Older hardware might take 5+ seconds for the same operation
- This represents optimal performance for CPU-bound tasks in Python
- Adding threads would NOT improve performance due to the GIL

Author's original estimate: ~5 seconds
Actual performance on M3 Pro: ~0.66 seconds (7.5x faster!)
"""

import time 

def countdown(n):
    """
    Perform a simple countdown operation.
    
    This function represents CPU-intensive work by decrementing
    a counter in a tight loop. It's designed to stress the CPU
    without any I/O operations.
    
    Args:
        n (int): Starting number to countdown from
        
    Returns:
        None: Function completes when n reaches 0
    """
    while n > 0:
        n -= 1

# Configuration: 50 million iterations
# This number is chosen to create measurable execution time
# while being large enough to demonstrate performance differences
COUNT = 50000000

# Benchmark the sequential execution
start = time.time()
countdown(COUNT)
end = time.time()

# Display execution time
execution_time = end - start
print(f"Sequential execution time: {execution_time:.4f} seconds")
print(f"Operations per second: {COUNT/execution_time:,.0f}")