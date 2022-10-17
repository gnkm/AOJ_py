"""
7_B : How many ways?

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/7/ITP1_7_B

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    while True:
        n, x = map(int, input())
        if n == 0 and x == 0:
            sys.exit()

        count = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j <= i:
                    continue
                for k in range(1, n + 1):
                    if k <= i or k <= j:
                        continue
                    if i + j + k == x:
                        count += 1

        print(count)


if __name__ == '__main__':
    main()
