import time

def decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} call executed in {end_time - start_time:.6f} sec")
    return wrapper
