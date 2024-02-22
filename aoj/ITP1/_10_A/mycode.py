"""
10_A : Distance

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_A

Result: AC
"""

import pkg_resources
if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic

import math
import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    x1, y1, x2, y2 = map(float, input())
    print(f'{math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2):.6f}')


if __name__ == '__main__':
    main()
