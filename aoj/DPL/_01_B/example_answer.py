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
i_mesli = lambda: list(map(int, input()))
i_memli = lambda n: [i_mesli() for _ in range(n)]


def main():
    N, W = i_mesli()
    items = i_memli(N)
    # @TODO: Implement
    sys.exit()


if __name__ == "__main__":
    main()
