"""ALDS1_4_B < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_4_B

ALDS1_4_B < Resources | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/resources/commentaries/ALDS1_4_B/ja/post?general=Algorithm

二分探索がテーマ。

Result: AC
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    _ = i_sesli()
    seq1 = i_mesli()
    _ = i_sesli()
    seq2 = i_mesli()
    series = list(set(seq1))
    ans = 0
    for num in seq2:
        if binary_search(num, series):
            ans += 1

    print(ans)
    sys.exit()


def binary_search(key, series):
    left = 0
    right = len(series)
    while left < right:
        mid = (left + right) // 2
        if series[mid] == key:
            return mid
        elif key < series[mid]:
            right = mid
        else:
            left = mid + 1
    return None


if __name__ == "__main__":
    main()
