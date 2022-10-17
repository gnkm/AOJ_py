"""
Circle

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/4/ITP1_4_B

Result: Wrong Answer(# 1)
"""

from decimal import Context, Decimal, getcontext
import math
import sys

PREC = 8
getcontext().prec = PREC
input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesls = lambda: str(input()[0])

def main():
    context = Context(prec=PREC)
    pi = context.create_decimal_from_float(math.pi)
    r = Decimal(i_sesls())
    area = pi * r ** 2
    circumference = Decimal('2') * pi * r
    print(f'{area} {circumference}')


if __name__ == '__main__':
    main()
