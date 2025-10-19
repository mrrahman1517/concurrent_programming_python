import time
import requests
from concurrent.futures import ThreadPoolExecutor
import asyncio
import aiohttp

# List of URLs to fetch (using httpbin.org for testing)
URLS = [
    "https://httpbin.org/delay/1",  # Simulates 1-second delay
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]

def fetch_url(url):
    """Fetch a single URL - simulates I/O-bound work"""
    try:
        response = requests.get(url, timeout=10)
        return f"Status: {response.status_code} for {url}"
    except Exception as e:
        return f"Error: {e} for {url}"

def sequential_fetch():
    """Sequential approach - one request at a time"""
    print("Sequential I/O-bound operations:")
    print("=" * 40)
    
    start = time.time()
    results = []
    
    for url in URLS:
        result = fetch_url(url)
        results.append(result)
        print(f"Completed: {url}")
    
    end = time.time()
    duration = end - start
    print(f"\nSequential total time: {duration:.2f} seconds")
    return duration

def threaded_fetch():
    """Threaded approach - multiple requests concurrently"""
    print("\nThreaded I/O-bound operations:")
    print("=" * 40)
    
    start = time.time()
    
    # Using ThreadPoolExecutor for cleaner thread management
    with ThreadPoolExecutor(max_workers=8) as executor:
        # Submit all requests
        future_to_url = {executor.submit(fetch_url, url): url for url in URLS}
        
        # Collect results as they complete
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
    """Async version of fetch_url"""
    try:
        async with session.get(url) as response:
            return f"Status: {response.status} for {url}"
    except Exception as e:
        return f"Error: {e} for {url}"

async def async_fetch():
    """Async approach using aiohttp"""
    print("\nAsync I/O-bound operations:")
    print("=" * 40)
    
    start = time.time()
    
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
        # Create tasks for all URLs
        tasks = [async_fetch_url(session, url) for url in URLS]
        
        # Wait for all tasks to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, result in enumerate(results):
            print(f"Completed: {URLS[i]}")
    
    end = time.time()
    duration = end - start
    print(f"\nAsync total time: {duration:.2f} seconds")
    return duration

def main():
    print("I/O-Bound Performance Comparison")
    print("=" * 50)
    print("Fetching 8 URLs, each with 1-second delay\n")
    
    # Test sequential approach
    seq_time = sequential_fetch()
    
    # Test threaded approach
    threaded_time = threaded_fetch()
    
    # Test async approach
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
    
    # Summary
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

if __name__ == "__main__":
    main()