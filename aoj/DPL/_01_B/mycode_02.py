"""DPL_1_B < Library < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_B
2024-04-10 解き直し

Result: WA
"""

try:
    import icecream

    debug = icecream.ic
except Exception:
    debug = print

import sys

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: list(map(int, input()))
i_memli = lambda n: [i_mesli() for _ in range(n)]


def main():
    N, W = i_mesli()
    items = i_memli(N)
    # values: 重さ w の時の価値の最大値
    # values[w] = value
    # values[W] が解答になる
    values = {i: 0 for i in range(W + 1)}

    for weight_org, value_org in values.items():
        for item_info in items:
            value_item = item_info[0]
            weight_item = item_info[1]
            if weight_item + weight_org <= W:
                values[weight_org + weight_item] = max(
                    values[weight_org + weight_item], value_org + value_item
                )
            # print(f"{weight_org = }, {weight_item = }")
            # print(values)

    print(values[W])
    sys.exit()


if __name__ == "__main__":
    main()
