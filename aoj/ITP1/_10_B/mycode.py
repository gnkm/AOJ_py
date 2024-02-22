"""
10_B : Triangle

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_B

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
    a, b, corner_ab_degree = map(int, input())
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(corner_ab_degree)))

    S = 1 / 2 * a * b * math.sin(math.radians(corner_ab_degree))
    L = a + b + c
    h = 2 * S / a

    print(f'{S:.5f} {L:.5f} {h:.5f}')


if __name__ == '__main__':
    main()
