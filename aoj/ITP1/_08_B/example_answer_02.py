"""
8_B : Sum of Numbers

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_B
https://onlinejudge.u-aizu.ac.jp/solutions/problem/ITP1_8_B/review/3216166/jakenu0x5e/Python3
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
i_sesls = lambda: str(input())

def main():
    while True:
        number = i_sesls()
        if number == '0':
            sys.exit()

        print(
            sum(
                map(int, number)
            )
        )

        # print(list(map(int, number)))  # => [1, 2, 3]
        # print(list('hoge'))  # => ['h', 'o', 'g', 'e']


if __name__ == '__main__':
    main()
