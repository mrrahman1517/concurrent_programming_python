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
