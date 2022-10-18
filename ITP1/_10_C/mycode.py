"""
10_C : Standard Deviation

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_C

Result:
"""

import pkg_resources
if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic

import math
import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    while True:
        n = i_sesli()
        if n == 0:
            sys.exit()

        nums = i_mesli()
        mean = 1 / n * sum(nums)
        deviation = math.sqrt(1 / n * sum([(e - mean) ** 2 for e in nums]))
        print(f'{deviation:.5f}')


if __name__ == '__main__':
    main()
