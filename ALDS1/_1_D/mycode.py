"""
最大の利益

https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_1_D

Result: time limit error
"""

import icecream, pprint  # for debugging
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

INF = float('inf')

def main(prices):
    max_return = - INF
    for i, price in enumerate(prices):
        if i == len(prices) - 1:
            break

        compared_prices = prices[i + 1:]
        diffs = list(map(lambda x: x - price, compared_prices))
        max_return = max(max_return, max(diffs))

    return max_return


if __name__ == '__main__':
    n = i_sesli()
    prices = i_semli(n)
    max_return = main(prices)
    print(max_return)
