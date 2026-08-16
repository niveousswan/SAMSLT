from time import perf_counter
from contextlib import contextmanager

@contextmanager
def timed(result, key):
    t = perf_counter()
    yield
    result[key] = perf_counter() - t
