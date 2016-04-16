from functools import lru_cache, wraps

import sys
import time


def write_time_to(writer):
    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            writer.write(str(duration) + "\n")
            return result
        return wrapper
    return timeit


def hello():
    return 'Hello'


cache_func = lru_cache(maxsize=32)(hello)
write_func = write_time_to(sys.stdout)(cache_func)
res1 = write_func()

res2 = write_time_to(sys.stdout)(lru_cache(maxsize=32)(hello))


