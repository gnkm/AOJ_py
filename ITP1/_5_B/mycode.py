"""
Print a Frame

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/5/ITP1_5_B

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()

BOUNDARY = '#'
INSIDE = '.'


def main():
    while True:
        H, W = map(int, input())
        if H == 0 and W == 0:
            sys.exit()

        rectangle_lines = make_rectangle_lines(H, W)
        for s in rectangle_lines :
            print(s)
        print('')


def make_rectangle_lines(H, W):
    rectangle_lines = []
    line_num = 1
    for _ in range(1, H + 1):
        col_num = 1
        line_str = ''
        for _ in range(1, W + 1):
            if line_num == 1 or line_num == H:
                line_str += BOUNDARY
            elif col_num == 1 or col_num == W:
                line_str += BOUNDARY
            else:
                line_str += INSIDE

            col_num += 1

        rectangle_lines.append(line_str)
        line_num += 1

    return rectangle_lines


if __name__ == '__main__':
    main()
