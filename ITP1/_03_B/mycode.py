"""
Print Test Cases

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/3/ITP1_3_B
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])


def main():
    # x = input()  # => ['3']
    # x = map(int, input())  # => <map object at 0x1016533d0>
    # [x] = map(int, input())  # => 3
    i = 1
    while True:
        # [num] = map(int, input())
        num = i_sesli()
        if num == 0:
            sys.exit()

        print(f'Case {i}: {num}')
        i += 1


if __name__ == '__main__':
    main()
