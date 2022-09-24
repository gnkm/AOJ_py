"""
Min, Max and Sum

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/4/ITP1_4_D

Result:
"""


import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))

def main():
    _ = i_sesli()
    nums = i_mesli()
    print(f'{min(nums)} {max(nums)} {sum(nums)}')


if __name__ == '__main__':
    main()
