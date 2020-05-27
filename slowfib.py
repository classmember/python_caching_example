def slowfib(n):
    '''Fibonacci Sequence with no caching'''
    if (n<=0):
        return 0
    if (n==1):
        return 1
    else:
        return slowfib(n-2) + slowfib(n-1)
