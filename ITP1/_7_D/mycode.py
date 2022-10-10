"""
7_D : Matrix Multiplication

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/7/ITP1_7_D

Result:
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, input()))
i_memli = lambda n: [i_mesli() for _ in range(n)]


def main():
    n, m, l = map(int, input())
    matrix_A = i_memli(n)
    matrix_B = i_memli(m)

    matrix_C = []
    for i in range(n):
        c_row = []
        for j in range(l):
            c_ij = 0
            for k in range(m):
                c_ij += matrix_A[i][k] * matrix_B[k][j]

            c_row.append(c_ij)
        matrix_C.append(c_row)

    for row in matrix_C:
        print(' '.join(list(map(str, row))))


if __name__ == '__main__':
    main()
