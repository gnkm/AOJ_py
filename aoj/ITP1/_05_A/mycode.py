"""
Print a Rectangle

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/5/ITP1_5_A

Result:
"""


import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    while True:
        H, W = map(int, input())
        if H == 0 and W == 0:
            sys.exit()

        for _ in range(H):
            one_line = ''
            for _ in range(W):
                one_line += '#'

            print(one_line)
        print('')


if __name__ == '__main__':
    main()
