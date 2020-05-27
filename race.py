#!/usr/bin/python3.8
from sys import argv
from time import time_ns
from fib import fib
from slowfib import slowfib


def run_fib(i):
    race_one_start = time_ns()
    race_one_results = fib(i)
    race_one_finish = time_ns()
    time_one = (race_one_finish - race_one_start) / 1e9
    print(f">>> fib({i})")
    print(f"{race_one_results}")
    print(f"  info: {fib.__doc__}")
    print(f"  time: {time_one} seconds\n")


def run_slowfib(i):
    race_two_start = time_ns()
    race_two_results = slowfib(i)
    race_two_finish = time_ns()
    time_two = (race_two_finish - race_two_start) / 1e9
    print(f">>> slowfib({i})")
    print(f"{race_two_results}")
    print(f"  info: {slowfib.__doc__}")
    print(f"  time: {time_two} seconds\n")


def main(i):
    '''Race between fib functions'''
    run_fib(i)
    run_slowfib(i)


if (__name__ == '__main__'):
    usage ='''usage: race (number of iterations between 0 and 498)'''
    argc = len(argv)
    if (argc >= 2):
        cycles = int(argv[1])
        if isinstance(cycles, int):
            main(cycles)
        else:
            print(usage)
    else:
        print(usage)
