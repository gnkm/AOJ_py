"""
6_D : Matrix Vector Multiplication

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/6/ITP1_6_D

Result:
"""

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_semli = lambda n: [i_sesli() for _ in range(n)]
i_mesli = lambda: list(map(int, input()))
i_memli = lambda n: [i_mesli() for _ in range(n)]


def main():
    n, m = map(int, input())
    A_matrix = i_memli(n)
    b_vector = i_semli(m)
    c_vector = []
    for row in A_matrix:
        c_i = 0
        for i, _ in enumerate(row):
            c_i += row[i] * b_vector[i]
        c_vector.append(c_i)

    for e in c_vector:
        print(e)


if __name__ == '__main__':
    main()
