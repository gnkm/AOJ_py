"""ALDS1_3_A < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_3_A

Result: AC
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesls = lambda: list(input())


def main():
    operands = i_mesls()
    stack = []
    for operand in operands:
        if operand.isnumeric():
            stack.append(operand)
        else:
            num2 = stack.pop(-1)
            num1 = stack.pop(-1)
            val = eval(f"{num1} {operand} {num2}")
            stack.append(str(val))

    print(*stack)
    sys.exit()


if __name__ == "__main__":
    main()
