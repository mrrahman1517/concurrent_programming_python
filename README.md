<<<<<<< HEAD
# Python Concurrency Prep Plan

This package contains 10-day guided exercises for mastering Python concurrency interview skills.

Refer to day-by-day schedule in chat and use the video playlist:

- [Python Concurrency: from beginner to pro](https://www.youtube.com/watch?v=18B1pznaU1o)
- [Producer-Consumer pattern](https://www.youtube.com/watch?v=SO_Yc5bydgI)
- [Concurrency Concepts in Python](https://www.youtube.com/watch?v=S05-MZAJqNM)
- [Threading Tutorial: Basic to Advanced](https://www.youtube.com/watch?v=Rm9Pic2rpAQ)
- [Parallel Programming in Python: Practical Guide](https://www.youtube.com/watch?v=IQxKjGEVteI)


---

## Setup

See **SETUP.md** for virtualenv and tooling instructions. A `requirements.txt` is provided for optional dev tools.
=======
# Python Concurrency Examples - GIL Demonstration

This repository contains educational examples demonstrating the Global Interpreter Lock (GIL) in Python and how it affects different types of workloads.

## Python Concurrency: Guided Exercises & GIL Demonstrations

This repository combines two educational resources:

1. **10-day Guided Exercises for Python Concurrency Interview Skills**
	- A structured set of daily exercises to master Python concurrency concepts, patterns, and interview questions.
	- See **SETUP.md** for environment setup and `requirements.txt` for optional dev tools.
	- Video playlist references:
	  - [Python Concurrency: from beginner to pro](https://www.youtube.com/watch?v=18B1pznaU1o)
	  - [Producer-Consumer pattern](https://www.youtube.com/watch?v=SO_Yc5bydgI)
	  - [Concurrency Concepts in Python](https://www.youtube.com/watch?v=S05-MZAJqNM)
	  - [Threading Tutorial: Basic to Advanced](https://www.youtube.com/watch?v=Rm9Pic2rpAQ)
	  - [Parallel Programming in Python: Practical Guide](https://www.youtube.com/watch?v=IQxKjGEVteI)

2. **GIL (Global Interpreter Lock) Demonstration Programs**
	- Educational examples showing how Python's GIL affects multi-threading for CPU-bound and I/O-bound tasks.
	- Includes benchmarks, explanations, and real-world scenarios.

---

## 📚 GIL Demonstration Overview

The Python GIL (Global Interpreter Lock) impacts how Python handles multi-threading:
- **CPU-bound tasks**: Threading does not improve performance due to the GIL.
- **I/O-bound tasks**: Threading can provide major speedups as the GIL is released during I/O waits.

### Included Programs

- `seq.py`: Sequential CPU-bound baseline
- `threaded.py`: Multi-threaded CPU-bound (shows GIL impact)
- `simple_io.py`: Local I/O-bound threading demo
- `io_bound.py`: Real-world network I/O comparison

Each program includes detailed output and timing information.

---

## 🔬 Key Findings

| Task Type      | Threading Benefit | Why                              |
| -------------- | ---------------- | --------------------------------- |
| CPU-bound      | ❌ None          | GIL prevents parallel execution   |
| I/O-bound      | ✅ Major speedup | GIL released during I/O operations|

### When to Use Threading
- File I/O, network requests, user input, or any operation waiting for external resources.

### When Not to Use Threading
- Mathematical computations, image/data processing, or CPU-intensive pure Python code.
- Use `multiprocessing`, NumPy/SciPy, Cython, or PyPy for CPU-bound tasks.

---

## 🏃‍♂️ Running the Examples

```bash
# Run individual examples
python seq.py           # Baseline CPU-bound performance
python threaded.py      # Show GIL impact on CPU tasks
python simple_io.py     # Local I/O threading demo
python io_bound.py      # Real-world network I/O demo
```

---

## 🎯 Educational Goals

This repository helps you:
1. Master Python concurrency for interviews and real-world use
2. Understand the GIL and its impact on threading
3. Learn when to use threading vs. multiprocessing
4. Benchmark and compare concurrency approaches

---

## Setup

See **SETUP.md** for virtualenv and tooling instructions. A `requirements.txt` is provided for optional dev tools.

---

## � Further Reading

- [Python GIL Documentation](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
- [Real Python: Python's GIL](https://realpython.com/python-gil/)
- [Concurrency vs Parallelism](https://blog.golang.org/waza-talk)

---

*This educational repository demonstrates fundamental Python concurrency concepts with practical, runnable examples and a guided 10-day exercise plan.*
## 💡 When to Use Each Approach
- File I/O operations
- Network requests (HTTP, database)
- User input waiting
- Any operation that waits for external resources

### Don't Use Threading For:
- Mathematical computations
- Image/data processing
- Tight loops with calculations
- CPU-intensive pure Python code

### Alternatives for CPU-bound Tasks:
- `multiprocessing` (separate processes, no GIL)
- NumPy/SciPy (C extensions that release GIL)
- Cython (compiled extensions)
- PyPy (JIT compiler)

## 🏃‍♂️ Running the Examples

```bash
# Run individual examples
python seq.py           # Baseline CPU-bound performance
python threaded.py      # Show GIL impact on CPU tasks
python simple_io.py     # Local I/O threading demo
python io_bound.py      # Real-world network I/O demo

# All examples include detailed output and timing information
```

## 🎯 Educational Goals

This repository helps you understand:

1. **The GIL Limitation**: Why CPU-bound Python code doesn't benefit from threading
2. **I/O Concurrency**: How threading dramatically improves I/O-bound performance
3. **Real-world Application**: When to choose threading vs other approaches
4. **Performance Measurement**: How to benchmark and compare different approaches

## 📊 Expected Results Summary

- **CPU-bound (seq.py)**: ~0.66s baseline
- **CPU-bound threaded**: ~0.67s (no improvement)
- **I/O-bound sequential**: ~4-8s (slow)
- **I/O-bound threaded**: ~0.5-2s (much faster!)

## 🤔 Why Such Fast Performance?

The original author estimated 5 seconds for the CPU-bound task, but modern hardware (like Apple M3 Pro) runs it in ~0.66s due to:

- **Superior CPU performance** (modern architecture)
- **Python optimizations** (version 3.12.10 improvements)
- **System efficiency** (optimized OS and hardware)

This 7.5x performance difference demonstrates how hardware and software improvements compound over time!

## 📖 Further Reading

- [Python GIL Documentation](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
- [Real Python: Python's GIL](https://realpython.com/python-gil/)
- [Concurrency vs Parallelism](https://blog.golang.org/waza-talk)

---

*This educational repository demonstrates fundamental Python concurrency concepts with practical, runnable examples.*
>>>>>>> upstream/main
