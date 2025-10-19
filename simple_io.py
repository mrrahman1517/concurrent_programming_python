import time
from concurrent.futures import ThreadPoolExecutor

def simulate_file_operation(file_id, duration=0.5):
    """Simulate a file I/O operation with sleep"""
    print(f"Starting file operation {file_id}")
    time.sleep(duration)  # Simulates I/O wait time
    print(f"Completed file operation {file_id}")
    return f"Result from file {file_id}"

def sequential_io():
    """Sequential I/O operations"""
    print("Sequential I/O operations:")
    print("=" * 30)
    
    start = time.time()
    results = []
    
    for i in range(8):
        result = simulate_file_operation(i)
        results.append(result)
    
    end = time.time()
    duration = end - start
    print(f"\nSequential total time: {duration:.2f} seconds")
    return duration

def threaded_io():
    """Threaded I/O operations"""
    print("\nThreaded I/O operations:")
    print("=" * 30)
    
    start = time.time()
    
    with ThreadPoolExecutor(max_workers=8) as executor:
        # Submit all operations
        futures = [executor.submit(simulate_file_operation, i) for i in range(8)]
        
        # Wait for all to complete
        [future.result() for future in futures]
    
    end = time.time()
    duration = end - start
    print(f"\nThreaded total time: {duration:.2f} seconds")
    return duration

def main():
    print("Local I/O-Bound Performance Comparison")
    print("=" * 45)
    print("Simulating 8 file operations, each taking 0.5 seconds\n")
    
    seq_time = sequential_io()
    threaded_time = threaded_io()
    
    print("\n" + "=" * 45)
    print("PERFORMANCE SUMMARY:")
    print("=" * 45)
    print(f"Sequential time: {seq_time:.2f}s (expected ~4.0s)")
    print(f"Threaded time:   {threaded_time:.2f}s (expected ~0.5s)")
    
    speedup = seq_time / threaded_time
    print(f"\nThreading speedup: {speedup:.1f}x faster!")
    
    print("\nWhy threading works here:")
    print("- During time.sleep() (simulating I/O), the GIL is RELEASED")
    print("- Other threads can run while one thread waits for I/O")
    print("- True concurrency is achieved for I/O-bound tasks")

if __name__ == "__main__":
    main()