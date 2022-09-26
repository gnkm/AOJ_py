"""
Print a Chessboard

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/5/ITP1_5_C

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()

FIRST = '#'
SECOND = '.'


def main():
    while True:
        H, W = map(int, input())
        if H == 0 and W == 0:
            sys.exit()

        chessboard_lines = make_chessboard_lines(H, W)
        for s in chessboard_lines:
            print(s)
        print('')


def make_chessboard_lines(H, W):
    chessboard_lines = []
    line_num = 1
    for _ in range(1, H + 1):
        col_num = 1
        line_str = ''
        for _ in range(1, W + 1):
            if is_odd(line_num) and is_odd(col_num):
                line_str += FIRST
            elif is_odd(line_num) and is_even(col_num):
                line_str += SECOND
            elif is_even(line_num) and is_odd(col_num):
                line_str += SECOND
            elif is_even(line_num) and is_even(col_num):
                line_str += FIRST

            col_num += 1

        chessboard_lines.append(line_str)
        line_num += 1

    return chessboard_lines


def is_odd(num):
    return num % 2 == 1


def is_even(num):
    return num % 2 == 0


if __name__ == '__main__':
    main()
