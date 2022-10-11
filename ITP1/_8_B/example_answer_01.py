"""
8_B : Sum of Numbers

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_B
https://onlinejudge.u-aizu.ac.jp/solutions/problem/ITP1_8_B/review/6636668/naoto172/Python3
"""

import sys


def main():
    while True:
        N = input()
        if len(N) == 1 and int(N) == 0:
            break
        sum = 0
        for i in range(len(N)):
            sum += int(N[i])

        print(sum)


if __name__ == '__main__':
    main()
