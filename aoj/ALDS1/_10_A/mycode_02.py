"""
10_A : Fibonacci Number

https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_10_A

Result: AC

lru_cache 使用。
"""

# for debugging
import icecream
debug = icecream.ic

# submit the following code
from functools import lru_cache
import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    number = int(input()[0])
    print(nth_fibonacci(number))
    sys.exit()


@lru_cache(maxsize=None)
def nth_fibonacci(number):
    if number < 2:
        return 1
    return nth_fibonacci(number - 1) + nth_fibonacci(number - 2)


if __name__ == '__main__':
    main()
