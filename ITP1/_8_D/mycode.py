"""
8_D : Ring8_C : Counting Characters

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_8_D

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesls = lambda: input()[0]


def main():
    straw_org = i_sesls()
    needle = i_sesls()
    straw  = straw_org * 2
    if needle in straw:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
