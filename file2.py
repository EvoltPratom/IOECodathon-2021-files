import functools
import math
import sys


@functools.lru_cache(maxsize=None)
def fact(x):
    return math.factorial(x)


m = int(input())
n = int(input())


def myfunc(m, n):
    for i in range(200, 1, -1):
        if fact(m) % n**i == 0:
            return i


sys.stdout.write(str(myfunc(m, n)))
