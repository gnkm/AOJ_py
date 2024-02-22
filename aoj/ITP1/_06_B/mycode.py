"""
Finding Missing Cards

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/6/ITP1_6_B

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesls = lambda: list(input())
i_memls = lambda n: [i_mesls() for _ in range(n)]

SUITS = ['S', 'H', 'C', 'D']
RANKS = [i for i in range(1, 13 + 1)]
ALL_CARDS = [f'{suit} {rank}' for suit in SUITS for rank in RANKS]

def main():
    n = i_sesli()
    exists_cards_org = i_memls(n)
    exists_cards = [f'{c[0]} {c[1]}' for c in exists_cards_org]
    lost_cards = []
    for c in ALL_CARDS:
        if c not in exists_cards:
            lost_cards.append(c)

    for lc in lost_cards:
        print(lc)


if __name__ == '__main__':
    main()
