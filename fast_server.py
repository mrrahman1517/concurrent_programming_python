"""
fast_server.py
A high-throughput Fibonacci microservice server using multiprocessing and a fast Fibonacci algorithm.

This server uses a process pool to handle CPU-bound Fibonacci requests in parallel, utilizing all CPU cores.
"""

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from typing import Tuple
from concurrent.futures import ProcessPoolExecutor
import sys


def fib_fast(n: int) -> int:
    """
    Compute the nth Fibonacci number using an efficient iterative algorithm.
    """
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


def handle_client(client: socket, pool: ProcessPoolExecutor) -> None:
    """
    Handle a client connection: receive a number, compute Fibonacci in a process, send result.
    """
    while True:
        req: bytes = client.recv(100)
        if not req:
            break
        try:
            n: int = int(req)
        except ValueError:
            client.sendall(b'Invalid input\n')
            continue
        # Submit the computation to the process pool
        future = pool.submit(fib_fast, n)
        result: int = future.result()
        resp: bytes = str(result).encode("ascii") + b'\n'
        client.sendall(resp)
    client.close()
    print("Closed")


def fast_fib_server(address: Tuple[str, int], max_workers: int = None) -> None:
    """
    Start a TCP server that computes Fibonacci numbers using a process pool for high throughput.
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    print(f"Fast Fibonacci server listening on {address}")
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        while True:
            client, addr = sock.accept()
            print("Connection", addr)
            # Each client handled in a new thread, computation in a process
            from threading import Thread
            Thread(target=handle_client, args=(client, pool), daemon=True).start()


if __name__ == "__main__":
    # Example: run on localhost:25000 (or specify port as argument)
    host = "localhost"
    port = 25000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    fast_fib_server((host, port))
