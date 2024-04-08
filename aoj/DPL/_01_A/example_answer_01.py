"""DPL_1_A < Library < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_A

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

INF = float("inf")


def main():
    payment, coin_type_num = map(int, input().split())
    coins = mapl(int, input().split())
    table = [INF] * (payment + 1)
    table[0] = 0
    for coin in coins:
        for i in range(coin, payment + 1):
            table[i] = min(table[i], table[i - coin] + 1)
    print(table[payment])
    sys.exit()


if __name__ == "__main__":
    main()
