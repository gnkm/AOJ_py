"""
Swapping Two Numbers

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/3/ITP1_3_C
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, input()))


def main():
    while True:
        nums = i_mesli()
        if nums[0] == 0 and nums[1] == 0:
            sys.exit()

        nums.sort()
        print(f'{nums[0]} {nums[1]}')


if __name__ == '__main__':
    main()
