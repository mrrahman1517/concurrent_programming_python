import threading

def map_fn(chunk):
    return [x * x for x in chunk]

def reduce_fn(results):
    total = 0
    for r in results:
        total += sum(r)
    return total

def parallel_map_reduce(data, num_threads=4):
    chunk_size = len(data) // num_threads
    threads = []
    result_list = [None] * num_threads

    def worker(i, chunk):
        result_list[i] = map_fn(chunk)

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        t = threading.Thread(target=worker, args=(i, data[start:end]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return reduce_fn(result_list)

if __name__ == "__main__":
    data = list(range(100000))
    total = parallel_map_reduce(data, num_threads=4)
    print("Total:", total)
