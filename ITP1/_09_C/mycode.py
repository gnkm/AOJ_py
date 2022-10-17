"""
9_C : Card Game

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_C

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesls = lambda: list(input())
i_memls = lambda n: [i_mesls() for _ in range(n)]


def main():
    number = i_sesli()
    words = i_memls(number)
    taro = 0
    hanako = 0
    for pair in words:
        if pair[0] < pair[1]:
            hanako += 3
        elif pair[0] == pair[1]:
            taro += 1
            hanako += 1
        else:
            taro += 3

    print(f'{taro} {hanako}')


if __name__ == '__main__':
    main()
