"""ALDS1_1_B < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_1_B
"""

try:
    import icecream

    debug = icecream.ic
except Exception:
    debug = print

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: list(map(int, input()))


def main():
    nums = i_mesli()
    num1 = max(nums)
    num2 = min(nums)
    print(gcd(num1, num2))
    sys.exit()


def gcd(num1, num2):
    _num1 = max(num1, num2)
    _num2 = min(num1, num2)
    if _num1 % _num2 == 0:
        return _num2
    return gcd(_num2, _num1 % _num2)


if __name__ == "__main__":
    main()
