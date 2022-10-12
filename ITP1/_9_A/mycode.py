"""
9_A : Finding a Word

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_A

Result: Wrong Answer
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesls = lambda: str(input()[0])
i_mesls = lambda: list(input())


def main():
    W = i_sesls()
    T = []
    while True:
        t = i_mesls()
        if t[0] == 'END_OF_TEXT':
            break
        T += list(map(lambda x: x.lower(), t))

    print(
        len(
            list(
                filter(lambda x: x == W, T)
            )
        )
    )


if __name__ == '__main__':
    main()
