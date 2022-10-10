"""
8_A : Toggling Cases

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_A

Result:
"""

import sys

_input = lambda: sys.stdin.readline().rstrip('\r\n')


def main():
    input_string = _input()
    print(input_string.swapcase())


if __name__ == '__main__':
    main()
