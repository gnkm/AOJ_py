"""
7_A : Grading

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/7/ITP1_7_A

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    while True:
        m, f, r = map(int, input())
        if m == -1 and f == -1 and r == -1:
            sys.exit()

        if -1 in [m, f]:
            result = 'F'
        elif 80 <= m + f:
            result = 'A'
        elif 65 <= m + f < 80:
            result = 'B'
        elif 50 <= m + f < 65:
            result = 'C'
        elif 30 <= m + f < 50:
            if r >= 50:
                result = 'C'
            else:
                result = 'D'
        else:
            result = 'F'

        print(result)


if __name__ == '__main__':
    main()
