"""
大小関係

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/2/ITP1_2_A
"""

import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
sys.setrecursionlimit(1000000)


def main():
    a, b = map(int, input())
    if a < b:
        print('a < b')
    elif a == b:
        print('a == b')
    else:
        print('a > b')


if __name__ == '__main__':
    main()
