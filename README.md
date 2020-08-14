# Python Recursive Fibonacci Sequences

## code
`fib.py`
```
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

```

### launch

run the faster version of fibonacci using caching

`$ ./launch.py 498`
```
>>> fib(498)
53254932961459429406936070704742495854129188261636423939579059478176515507039697978099330699648074089624
  info: Fibonacci Sequence with Least Recently Used Cache
  time: 0.000628 seconds

```

### race

run the both versions of the fibonacci using caching and non-caching versions

`./race.py`
```usage: launch (number of iterations between 0 and 498)```

`$ ./race.py 45`
```
>>> fib(45)
1134903170
  info: Fibonacci Sequence with Least Recently Used Cache
  time: 1.49e-05 seconds (0.000149 seconds)

>>> slowfib(45)
1134903170
  info: Fibonacci Sequence with no caching
  time: 301.9936715 seconds

```

## Limitations

Python has no Tail Call Recursion (TCO) feature, so the recursions have a built-in limit. This was a design decision in the language by Guido Van Rossum in order to keep the tracebacks in errors clear.

[python tco stackoverflow answer](https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion)
