"""
fib.py
Recursive Fibonacci function used by the server.
"""

def fib(n: int) -> int:
    """
    Compute the nth Fibonacci number recursively.
    Args:
        n (int): The position in the Fibonacci sequence (1-based).
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)