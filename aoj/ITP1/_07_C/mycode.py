"""
7_C : Spreadsheet

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/7/ITP1_7_C

Result:
"""

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, input()))
i_memli = lambda n: [i_mesli() for _ in range(n)]


def main():
    r, c = map(int, input())
    matrix = i_memli(r)

    printed_matrix = []
    for row in matrix:
        appended_row = row
        appended_row.append(sum(row))
        printed_matrix.append(appended_row)

    sum_cols = []
    for i in range(c + 1):
        sum_col = 0
        for row in printed_matrix:
            sum_col += row[i]
        sum_cols.append(sum_col)

    for row in printed_matrix:
        print(' '.join(list(map(str, row))))

    print(' '.join(list(map(str, sum_cols))))


if __name__ == '__main__':
    main()
