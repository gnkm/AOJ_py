"""
8_B : Sum of Numbers

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_B

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n')
i_sesls = lambda: str(input())


def main():
    while True:
        number = i_sesls()
        if number == '0':
            sys.exit()

        numbers = []
        for i in range(len(number)):
            numbers.append(
                int(number[i])
            )

        print(sum(numbers))


if __name__ == '__main__':
    main()
