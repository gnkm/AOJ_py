"""
A / B Problem

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/4/ITP1_4_A

Result: AC
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()

def main():
    a, b = map(int, input())
    print(f'{a // b} {a % b} {a / b:.6f}')


if __name__ == '__main__':
    main()
