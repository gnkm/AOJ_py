"""
最大の利益

https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_1_D

Result: time limit error
参照: プログラミングコンテスト攻略のためのアルゴリズムとデータ構造
方針
時系列を順に進んでいき、t - 1 以前の価格の最小値 P_min_t と P(t) を比べ小さい方を保持しておく。
また、t - 1 以前の利益の最大値 R_max_t と R(t) - P_min_t を比べ大きい方を保持しておく。
最終的に保持されていた利益の最大値が求められる値。
こうすることで O(n) の計算量ですませられる。
"""

import icecream, pprint  # for debugging
import random  # for generating some test cases
import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_seslf = lambda: float(input()[0])
i_sesls = lambda: str(input()[0])
i_semli = lambda n: [i_sesli() for _ in range(n)]
i_semlf = lambda n: [i_seslf() for _ in range(n)]
i_semls = lambda n: [i_sesls() for _ in range(n)]
i_mesli = lambda: list(map(int, input()))
i_meslf = lambda: list(map(float, input()))
i_mesls = lambda: list(input())
i_memli = lambda n: [i_mesli() for _ in range(n)]
i_memlf = lambda n: [i_meslf() for _ in range(n)]
i_memls = lambda n: [i_mesls() for _ in range(n)]

sys.setrecursionlimit(1000000)

def main(prices):
    # test_prices = []
    # for i in range(20):
    #     p = random.randrange(100, 1000, 50)
    #     test_prices.append(p)
    # print(test_prices)
    # sys.exit()

    # icecream.ic(prices)
    max_return = prices[1] - prices[0]
    min_price = prices[0]
    for i, price in enumerate(prices):
        if i == 0:
            continue

        max_return = max(max_return, price - min_price)
        min_price = min(min_price, price)
        # icecream.ic(i, price, max_return, min_price)

    return max_return


if __name__ == '__main__':
    n = i_sesli()
    prices = i_semli(n)
    max_return = main(prices)
    print(max_return)
