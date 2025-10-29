# Environment Setup

This repo's code samples use only the Python **standard library**.
The tools below are optional but recommended for a smoother workflow.

## 1) Create a virtual environment

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 2) Upgrade pip and install dev tools (optional)
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

This installs:
- **pytest** – run quick tests/experiments
- **mypy** – static type checking for exercises (helps with API clarity)
- **black** – code formatter
- **rich** – pretty printing/logs during practice

## 3) Run the examples
```bash
python day1_counter_lock.py
python day2_producer_consumer.py
python day3_lru_cache_threadsafe.py
python day4_threadpool_queue.py
python day5_parallel_map_reduce.py
```

## 4) (Optional) Format and type‑check
```bash
black .
mypy .
```

## 5) Troubleshooting
- If `mypy` reports missing type stubs, it's safe to ignore for these exercises.
- If you hit permission issues on Windows when activating the venv, open PowerShell **as Administrator** and run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
