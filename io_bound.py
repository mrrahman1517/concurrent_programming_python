"""
Real-World I/O-Bound Performance Comparison

This program demonstrates threading and async performance benefits using
real network I/O operations. Unlike the simulated I/O in simple_io.py,
this uses actual HTTP requests to show real-world threading benefits.

Three Approaches Compared:
1. Sequential: One request at a time (slow)
2. Threading: Multiple requests using threads (fast)
3. Async: Multiple requests using asyncio (fastest)

Network I/O Characteristics:
- HTTP requests involve waiting for network responses
- During network waits, the GIL is released
- Multiple threads can wait for different requests simultaneously
- Async provides even better resource utilization

Expected Results:
- Sequential: ~8+ seconds (8 requests × 1s delay + network overhead)
- Threading: ~1-2 seconds (all requests run concurrently)
- Async: ~1-2 seconds (similar to threading, often slightly faster)

Key Learning:
This demonstrates why web scrapers, API clients, and database applications
benefit enormously from threading or async programming.
"""

import time
import requests
from concurrent.futures import ThreadPoolExecutor
import asyncio
import aiohttp

# List of URLs to fetch (using httpbin.org for testing)
# httpbin.org/delay/1 simulates a 1-second server processing delay
# This mimics real-world APIs that take time to process requests
URLS = [
    "https://httpbin.org/delay/1",  # Simulates 1-second server delay
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]

def fetch_url(url):
    """
    Fetch a single URL using the requests library.
    
    This represents real I/O-bound work:
    - Network socket operations release the GIL
    - Thread waits for server response
    - Other threads can make concurrent requests
    
    Args:
        url (str): URL to fetch
        
    Returns:
        str: Status message with response code or error
    """
    try:
        # The GIL is released during network I/O operations
        response = requests.get(url, timeout=10)
        return f"Status: {response.status_code} for {url}"
    except Exception as e:
        return f"Error: {e} for {url}"

def sequential_fetch():
    """
    Sequential approach - one HTTP request at a time.
    
    This is the traditional blocking approach where each request
    must complete before the next one begins. Total time is the
    sum of all individual request times.
    
    Expected time: 8+ seconds (8 × 1s delay + network overhead)
    
    Returns:
        float: Total execution time in seconds
    """
    print("Sequential I/O-bound operations:")
    print("=" * 40)
    
    start = time.time()
    results = []
    
    # Process URLs one by one - blocking approach
    for url in URLS:
        result = fetch_url(url)
        results.append(result)
        print(f"Completed: {url}")
    
    end = time.time()
    duration = end - start
    print(f"\nSequential total time: {duration:.2f} seconds")
    return duration

def threaded_fetch():
    """
    Threaded approach - multiple HTTP requests concurrently.
    
    ThreadPoolExecutor manages a pool of worker threads.
    Each thread can make an independent HTTP request.
    While one thread waits for a response, others can work.
    
    Expected time: ~1-2 seconds (time of slowest request)
    
    Returns:
        float: Total execution time in seconds
    """
    print("\nThreaded I/O-bound operations:")
    print("=" * 40)
    
    start = time.time()
    
    # Using ThreadPoolExecutor for cleaner thread management
    # max_workers=8 means up to 8 concurrent requests
    with ThreadPoolExecutor(max_workers=8) as executor:
        # Submit all requests to the thread pool
        # They start executing immediately in parallel
        future_to_url = {executor.submit(fetch_url, url): url for url in URLS}
        
        # Collect results as they complete
        # This waits for all requests to finish
        results = []
        for future in future_to_url:
            result = future.result()
            results.append(result)
            print(f"Completed: {future_to_url[future]}")
    
    end = time.time()
    duration = end - start
    print(f"\nThreaded total time: {duration:.2f} seconds")
    return duration

async def async_fetch_url(session, url):
    """
    Async version of fetch_url using aiohttp.
    
    This is a coroutine that can be awaited. When waiting
    for the network response, it yields control back to
    the event loop, allowing other coroutines to run.
    
    Args:
        session: aiohttp ClientSession for making requests
        url (str): URL to fetch
        
    Returns:
        str: Status message with response code or error
    """
    try:
        # async with automatically handles connection management
        # The await releases control during network I/O
        async with session.get(url) as response:
            return f"Status: {response.status} for {url}"
    except Exception as e:
        return f"Error: {e} for {url}"

async def async_fetch():
    """
    Async approach using asyncio and aiohttp.
    
    This uses Python's async/await syntax for concurrent I/O.
    Unlike threading, this runs in a single thread but uses
    cooperative multitasking to handle multiple requests.
    
    Often more efficient than threading for I/O-bound tasks:
    - Lower memory overhead (no thread stacks)
    - No GIL contention
    - Better resource utilization
    
    Expected time: ~1-2 seconds (similar to threading)
    
    Returns:
        float: Total execution time in seconds
    """
    print("\nAsync I/O-bound operations:")
    print("=" * 40)
    
    start = time.time()
    
    # Create an HTTP session for connection reuse
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
        # Create coroutine tasks for all URLs
        # These will run concurrently when awaited
        tasks = [async_fetch_url(session, url) for url in URLS]
        
        # Wait for all tasks to complete concurrently
        # asyncio.gather() runs all tasks simultaneously
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Display completion status
        for i, result in enumerate(results):
            print(f"Completed: {URLS[i]}")
    
    end = time.time()
    duration = end - start
    print(f"\nAsync total time: {duration:.2f} seconds")
    return duration

def main():
    """
    Main function to compare all three approaches.
    
    Demonstrates the performance difference between:
    1. Sequential blocking I/O
    2. Multi-threaded I/O (GIL released during network operations)
    3. Async I/O (cooperative multitasking)
    """
    print("I/O-Bound Performance Comparison")
    print("=" * 50)
    print("Fetching 8 URLs, each with 1-second delay\n")
    
    # Test sequential approach (slowest)
    seq_time = sequential_fetch()
    
    # Test threaded approach (much faster)
    threaded_time = threaded_fetch()
    
    # Test async approach (often fastest)
    print("\nInstalling aiohttp for async example...")
    import subprocess
    try:
        subprocess.run(["pip", "install", "aiohttp"], check=True, capture_output=True)
        print("aiohttp installed successfully!")
        
        # Run async version
        async_time = asyncio.run(async_fetch())
        
    except subprocess.CalledProcessError:
        print("Failed to install aiohttp, skipping async example")
        async_time = None
    except ImportError:
        print("aiohttp not available, skipping async example")
        async_time = None
    
    # Performance summary and analysis
    print("\n" + "=" * 50)
    print("PERFORMANCE SUMMARY:")
    print("=" * 50)
    print(f"Sequential time: {seq_time:.2f}s")
    print(f"Threaded time:   {threaded_time:.2f}s")
    if async_time:
        print(f"Async time:      {async_time:.2f}s")
    
    speedup = seq_time / threaded_time
    print(f"\nThreading speedup: {speedup:.1f}x faster!")
    
    if async_time:
        async_speedup = seq_time / async_time
        print(f"Async speedup:     {async_speedup:.1f}x faster!")
    
    # Educational summary
    print("\nKey Takeaways:")
    print("- Network I/O benefits enormously from concurrency")
    print("- Threading works because GIL is released during network operations")
    print("- Async can be even more efficient for high-concurrency scenarios")
    print("- Both approaches are vastly superior to sequential I/O")

if __name__ == "__main__":
    main()