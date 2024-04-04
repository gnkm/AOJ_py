"""DPL_1_B < Library < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_B

Result: $(result)
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

INF = float("inf")


def main():
    N, W = i_mesli()
    items = i_memli(N)
    # @TODO: Implement
    sys.exit()


if __name__ == "__main__":
    main()
