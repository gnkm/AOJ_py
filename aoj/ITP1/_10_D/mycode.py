"""
10_D : Distance II(ミンコフスキー距離)

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_D

Result: AC
"""

import pkg_resources
if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))
i_memli = lambda n: [i_mesli() for _ in range(n)]


def main():
    n = i_sesli()
    vectors = i_memli(2)
    vector_x = vectors[0]
    vector_y = vectors[1]
    for p in range(1, 3 + 1):
        print(f'{minkowskis_distance(vector_x, vector_y, p):.6f}')

    chebyshev = max([abs(vector_x[i] - vector_y[i]) for i in range(n)])
    print(f'{chebyshev:.6f}')


def minkowskis_distance(vector_x, vector_y, p):
    n = len(vector_x)
    return pow(
        sum([pow(abs(vector_x[i] - vector_y[i]), p) for i in range(n)]),
        1 / p
    )


if __name__ == '__main__':
    main()
