"""
A / B Problem

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/4/ITP1_4_A

Result: Wrong Answer(# 9)
"""

from decimal import Decimal, getcontext
import sys

getcontext().prec = 20
input = lambda: sys.stdin.readline().rstrip('\r\n').split()

def main():
    a, b = map(int, input())
    d = int(a / b)
    r = a % b
    a_str = str(a)
    b_str = str(b)
    f_str = Decimal(a_str) / Decimal(b_str)
    f = float(f_str)
    print(f'{d} {r} {f}')


if __name__ == '__main__':
    main()
