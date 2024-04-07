"""DPL_1_A < Library < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_A

@TODO: Modify
コインの額面が大きいものから順に使っていくのが必ずしもベストではない。

Result: WA
"""

import sys
from copy import deepcopy

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    payment, coin_type_num = map(int, input().split())
    coins = mapl(int, input().split())
    print(solve(payment, coins))
    sys.exit()


def solve(payment, coins):
    if sum(coins) == 0:
        return 0
    if payment == 0:
        return 0
    coins = sorted(coins)[::-1]
    print(f"{payment = }, {coins = }")
    if payment < coins[-2]:
        return payment
    for i, coin in enumerate(coins):
        if payment >= coin:
            coin_num = payment // coin
            rest_payment = payment - coin_num * coin
            rest_coins = deepcopy(coins)
            rest_coins[i] = 0
            return coin_num + solve(rest_payment, rest_coins)


if __name__ == "__main__":
    main()
