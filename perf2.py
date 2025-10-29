"""
perf2.py
Benchmark script for measuring throughput (requests per second) of the Fibonacci server.
Sends as many fast requests as possible and prints the number of requests per second.
"""

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time

# Connect to the server (adjust port as needed)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))

n = 0

def monitor() -> None:
    """
    Print the number of requests sent every second.
    """
    global n
    while True:
        time.sleep(1)
        print(f"{n} reqs/sec")
        n = 0

Thread(target=monitor, daemon=True).start()

while True:
    # Send a fast request for fib(1)
    sock.send(b'1')
    resp = sock.recv(100)
    n += 1
