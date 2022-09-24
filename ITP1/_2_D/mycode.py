"""
Circle in a Rectangle

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/2/ITP1_2_D
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
W, H, x, y, r = map(int, input())

def main():
    if x - r < 0:
        print('No')
        sys.exit()

    if x + r > W:
        print('No')
        sys.exit()

    if y - r < 0:
        print('No')
        sys.exit()

    if y + r > H:
        print('No')
        sys.exit()

    print('Yes')


if __name__ == '__main__':
    main()
