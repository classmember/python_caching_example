from functools import lru_cache


@lru_cache(maxsize=3)
def fib(n):
    '''Fibonacci Sequence with Least Recently Used Cache'''
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
