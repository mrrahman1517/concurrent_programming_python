# Concurrency Design Notes

## When to use each model in Python
- threading – good for I/O-bound tasks, many concurrent operations
- multiprocessing – for CPU-bound, bypasses GIL
- asyncio – for large number of I/O tasks, event-driven

## Trade-offs
- GIL: limits simultaneous Python bytecode execution in CPython
- Thread overhead: context switching, memory
- Lock contention: if many threads share data, performance suffers
- Process overhead: memory duplication, startup cost
- Async complexity: callback flows, coroutine management

## Example system: Concurrent Log Processor
- Subsystems A, B, C each produce logs → threads push to QueueA, QueueB, QueueC
- Coordinator thread loops: pop from A, then B, then C, process
- Buffering ensures resilience if one subsystem is slow
- Optional timeout: if subsystem B hasn’t produced within X ms, mark error and continue

## Key primitives
- threading.Lock, threading.RLock
- threading.Condition
- queue.Queue (thread-safe)
- concurrent.futures.ThreadPoolExecutor / ProcessPoolExecutor
- asyncio.Event, asyncio.Queue (if using async)

---

# Interview Questions (Day 1–5)

## Day 1: Counter with Lock
**Conceptual:**
- Why is a lock necessary when multiple threads increment a shared counter?
- What could go wrong if you remove the lock from the counter example?
- Explain the difference between `lock.acquire()`/`lock.release()` and using a lock as a context manager (`with lock:`).
- How does the Global Interpreter Lock (GIL) affect this example?
**Coding:**
- Implement a thread-safe counter in Python that can be safely incremented by multiple threads.

## Day 2: Producer-Consumer with Queue
**Conceptual:**
- What problem does the producer-consumer pattern solve?
- Why is `queue.Queue` used instead of a simple list?
- How does the consumer know when to stop?
- What would happen if you forgot to put the sentinel value in the queue?
- How would you modify the code to support multiple consumers?
**Coding:**
- Write a Python program with one producer and one consumer thread using a thread-safe queue. The producer should generate numbers 0–9, and the consumer should print them.

## Day 3: Thread-Safe LRU Cache
**Conceptual:**
- Why do we need a lock in the LRU cache implementation?
- What is the purpose of `OrderedDict.move_to_end()` in the cache?
- How does the cache ensure thread safety for both `get` and `put` operations?
- What would happen if two threads call `put` at the same time?
**Coding:**
- Implement a thread-safe LRU cache class in Python with `get` and `put` methods.

## Day 4: ThreadPoolExecutor and Queue
**Conceptual:**
- What is the advantage of using `ThreadPoolExecutor` over manually managing threads?
- Why is a queue used between the producer and consumer?
- How does the consumer know when to stop processing items?
- What would happen if you started more consumers than the number of sentinels?
- How does `future.result()` work in this context?
**Coding:**
- Write a Python script that uses `ThreadPoolExecutor` to process a list of numbers in parallel, squaring each number and printing the result.

## Day 5: Parallel Map-Reduce
**Conceptual:**
- What is the purpose of splitting data into chunks for parallel processing?
- How does the `parallel_map_reduce` function coordinate work between threads?
- Why is a separate `reduce_fn` used after mapping?
- What are the limitations of this approach in Python?
- How would you modify the code to use processes instead of threads for CPU-bound tasks?
**Coding:**
- Implement a parallel map-reduce in Python that computes the sum of squares of a list using multiple threads.
