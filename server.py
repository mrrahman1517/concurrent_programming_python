"""
server.py
Fibonacci microservice server. Run this file to start the Fibonacci server.

This server listens for TCP connections. For each connection, it reads a number from the client,
computes the Fibonacci number for that input, and sends the result back.
"""

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from typing import Tuple
from fib import fib
from threading import Thread


def fib_server(address: Tuple[str, int]) -> None:
    """
    Start a TCP server that computes Fibonacci numbers for incoming requests.
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        #fib_handler(client)
        Thread(target=fib_handler, args=(client,), ).start()


def fib_handler(client: socket) -> None:
    """
    Handle a client connection: receive a number, compute Fibonacci, send result.
    """
    while True:
        req: bytes = client.recv(100)
        if not req:
            break
        n: int = int(req)
        result: int = fib(n)
        resp: bytes = str(result).encode("ascii") + b'\n'
        client.sendall(resp)
    print("Closed")


if __name__ == "__main__":
    # Example: run on localhost:25000 (or specify port as argument)
    import sys
    host = "localhost"
    port = 25000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    print(f"Starting Fibonacci server on {host}:{port}")
    fib_server(('', port))
