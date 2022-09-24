"""
How Many Divisors?

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/3/ITP1_3_D
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()

def main():
    divisor_num = 0
    a, b, c = map(int, input())
    for n in range(a, b + 1):
        if c % n == 0:
            divisor_num += 1

    print(divisor_num)


if __name__ == '__main__':
    main()
