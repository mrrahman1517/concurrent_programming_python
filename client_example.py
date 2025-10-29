"""
client_example.py
A simple client to test the Fibonacci server (server.py or fast_server.py).
Sends a number to the server and prints the response.
"""

import socket
import sys

def send_fib_request(n: int, host: str = "localhost", port: int = 25000) -> None:
    """
    Connect to the Fibonacci server, send a number, and print the response.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(str(n).encode("ascii"))
        result = sock.recv(100)
        print(f"Fibonacci({n}) = {result.decode().strip()}")

if __name__ == "__main__":
    # Usage: python client_example.py 35 [host] [port]
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 35
    host = sys.argv[2] if len(sys.argv) > 2 else "localhost"
    port = int(sys.argv[3]) if len(sys.argv) > 3 else 25000
    send_fib_request(n, host, port)
