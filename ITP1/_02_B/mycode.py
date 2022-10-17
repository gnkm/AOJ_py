"""
Range

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/2/ITP1_2_B
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
a, b, c = map(int, input())
sys.setrecursionlimit(1000000)

def main():
    if a < b and b < c:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
