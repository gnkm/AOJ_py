"""
10_B : Triangle

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_B

Result: Runtime Error(#2)
Traceback (most recent call last): File "rep/code.py", line 20, in main() File "rep/code.py", line 10, in main c = math.sqrt(a ** 2 + b ** 2 - a * a * b * math.cos(math.radians(corner_ab_degree))) ValueError: math domain error 0.02user 0.00system 0:00.02elapsed 100%CPU (0avgtext+0avgdata 5704maxresident)k 0inputs+8outputs (0major+1790minor)pagefaults 0swaps
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
