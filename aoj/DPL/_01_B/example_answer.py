"""DPL_1_B < Library < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_B
https://onlinejudge.u-aizu.ac.jp/solutions/problem/DPL_1_B/review/4063442/naoto172/Python3

Result: AC
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: list(map(int, input()))
i_memli = lambda n: [i_mesli() for _ in range(n)]

INF = float("inf")


def main():
    N, W = i_mesli()
    items = i_memli(N)
    dp = [-INF] * (W + 1)
    dp[0] = 0
    for item_info in items:
        value_item = item_info[0]
        weight_item = item_info[1]
        for i in range(W, weight_item - 1, -1):
            if dp[i - weight_item] == -INF:
                continue
            dp[i] = max(dp[i], dp[i - weight_item] + value_item)

    print(max(dp))
    sys.exit()


if __name__ == "__main__":
    main()
