"""
I/O-Bound Threading Example - Demonstrating When Threading Works

This program demonstrates how threading CAN provide significant performance
improvements for I/O-bound tasks, in contrast to CPU-bound tasks.

Key Difference from CPU-bound tasks:
- During I/O operations (like time.sleep, file reads, network requests),
  the GIL is RELEASED, allowing other threads to run
- This enables true concurrency for I/O-waiting threads
- Multiple threads can wait for I/O simultaneously

Expected Results:
- Sequential: ~4.0 seconds (8 operations × 0.5s each)
- Threaded: ~0.5 seconds (all operations run concurrently)
- Speedup: ~8x faster!

Why This Works:
1. time.sleep() releases the GIL (simulates I/O wait)
2. Other threads can execute while one thread sleeps
3. All 8 operations run concurrently, not sequentially

Real-world I/O operations that benefit from threading:
- File read/write operations
- Network requests (HTTP, database queries)
- User input waiting
- Inter-process communication
"""

import time
from concurrent.futures import ThreadPoolExecutor

def simulate_file_operation(file_id, duration=0.5):
    """
    Simulate a file I/O operation using time.sleep().
    
    time.sleep() releases the GIL, allowing other threads to run.
    This simulates real I/O operations like:
    - Reading from disk
    - Network requests
    - Database queries
    
    Args:
        file_id (int): Identifier for this operation
        duration (float): Simulated I/O wait time in seconds
        
    Returns:
        str: Result message indicating completion
    """
    print(f"Starting file operation {file_id}")
    time.sleep(duration)  # GIL is RELEASED here - other threads can run!
    print(f"Completed file operation {file_id}")
    return f"Result from file {file_id}"

def sequential_io():
    """
    Execute I/O operations one at a time (sequential).
    
    This represents the traditional approach where each operation
    must complete before the next one begins.
    
    Expected time: 8 operations × 0.5s = 4.0 seconds
    """
    print("Sequential I/O operations:")
    print("=" * 30)
    
    start = time.time()
    results = []
    
    # Execute operations one by one
    for i in range(8):
        result = simulate_file_operation(i)
        results.append(result)
    
    end = time.time()
    duration = end - start
    print(f"\nSequential total time: {duration:.2f} seconds")
    return duration

def threaded_io():
    """
    Execute I/O operations concurrently using threads.
    
    ThreadPoolExecutor manages thread creation and cleanup.
    All operations start nearly simultaneously and run concurrently
    because the GIL is released during time.sleep().
    
    Expected time: ~0.5 seconds (duration of longest operation)
    """
    print("\nThreaded I/O operations:")
    print("=" * 30)
    
    start = time.time()
    
    # Use ThreadPoolExecutor for clean thread management
    with ThreadPoolExecutor(max_workers=8) as executor:
        # Submit all operations to thread pool
        # They will start executing immediately
        futures = [executor.submit(simulate_file_operation, i) for i in range(8)]
        
        # Wait for all operations to complete
        # This blocks until the slowest operation finishes
        [future.result() for future in futures]
    
    end = time.time()
    duration = end - start
    print(f"\nThreaded total time: {duration:.2f} seconds")
    return duration

def main():
    """
    Main function to demonstrate I/O-bound threading performance.
    
    Compares sequential vs threaded execution for the same workload
    to show dramatic performance improvement when GIL is released.
    """
    print("Local I/O-Bound Performance Comparison")
    print("=" * 45)
    print("Simulating 8 file operations, each taking 0.5 seconds\n")
    
    # Run both approaches with identical workloads
    seq_time = sequential_io()
    threaded_time = threaded_io()
    
    # Calculate and display performance improvement
    print("\n" + "=" * 45)
    print("PERFORMANCE SUMMARY:")
    print("=" * 45)
    print(f"Sequential time: {seq_time:.2f}s (expected ~4.0s)")
    print(f"Threaded time:   {threaded_time:.2f}s (expected ~0.5s)")
    
    speedup = seq_time / threaded_time
    print(f"\nThreading speedup: {speedup:.1f}x faster!")
    
    # Explain why threading works for I/O-bound tasks
    print("\nWhy threading works here:")
    print("- During time.sleep() (simulating I/O), the GIL is RELEASED")
    print("- Other threads can run while one thread waits for I/O")
    print("- True concurrency is achieved for I/O-bound tasks")
    print("- This is the opposite of CPU-bound tasks where GIL blocks concurrency")

if __name__ == "__main__":
    main()