"""
Simple Calculator

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/4/ITP1_4_C

Result: Wrong Answer(# 2)
"""

from decimal import Decimal, getcontext
import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesls = lambda: list(input())

getcontext().prec = 8

def main():
    while True:
        num_op_num = i_mesls()
        a_str = num_op_num[0]
        b_str = num_op_num[2]
        op = num_op_num[1]
        if op == '?':
            sys.exit()

        print(
            str(
                eval(
                    f'Decimal({a_str}) {op} Decimal({b_str})'
                )
            )
        )


if __name__ == '__main__':
    main()
