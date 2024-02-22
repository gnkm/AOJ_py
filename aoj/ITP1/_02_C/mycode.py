"""
Range

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/2/ITP1_2_B
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, input()))
sys.setrecursionlimit(1000000)

def main():
    nums = i_mesli()
    nums.sort()
    print(' '.join(map(str, nums)))


if __name__ == '__main__':
    main()
