"""
9_C : Card Game

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_C

Result:
"""

import functools
import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesls = lambda: list(input())
i_memls = lambda n: [i_mesls() for _ in range(n)]


def main():
    number = i_sesli()
    words = i_memls(number)
    scores_init = [0, 0]  # taro, hanako
    scores = functools.reduce(game, words, scores_init)
    print(' '.join(map(str, scores)))


def game(scores, pair):
    if pair[0] < pair[1]:
        scores[1] += 3
    elif pair[0] == pair[1]:
        scores[0] += 1
        scores[1] += 1
    else:
        scores[0] += 3

    return scores


if __name__ == '__main__':
    main()
