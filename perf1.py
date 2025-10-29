"""
perf1.py
Benchmark script for measuring latency of long-running requests to the Fibonacci server.
Sends repeated requests and prints the time taken for each response.
"""

from socket import socket, AF_INET, SOCK_STREAM
import time

# Connect to the server (adjust port as needed)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 26000))

while True:
    start = time.time()
    sock.send(b'30')  # Send a request for fib(30)
    resp = sock.recv(100)
    end = time.time()
    print(f"Response time: {end - start:.4f} seconds")
