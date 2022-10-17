"""
Reversing Numbers

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/6/ITP1_6_A

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesls = lambda: list(input())


def main():
    _ = i_sesli()
    org_list = i_mesls()
    print(' '.join(list(reversed(org_list))))


if __name__ == '__main__':
    main()
