"""ALDS1_1_B < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_1_B
"""

try:
    import icecream

    debug = icecream.ic
except Exception:
    debug = print

import sys
from math import gcd

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: list(map(int, input()))


def main():
    num1, num2 = i_mesli()
    print(gcd(num1, num2))
    sys.exit()


if __name__ == "__main__":
    main()
