"""
Structured Programming

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/5/ITP1_5_D

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])


def main():
    n = i_sesli()
    ret = ''
    for i in range(1, n + 1):
        if i % 3 == 0:
            ret += f' {i}'
            continue

        if '3' in str(i):
            ret += f' {i}'
            continue

    print(ret)


if __name__ == '__main__':
    main()
