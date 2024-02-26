"""ALDS1_4_B < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_4_B

Result: WA
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    # print(f"{binary_search(1, [1, 2, 3, 4, 5]) = }")
    # print(f"{binary_search(2, [1, 2, 3, 4, 5]) = }")
    # print(f"{binary_search(5, [1, 2, 3, 4, 5]) = }")
    # sys.exit()
    _ = i_sesli()
    seq1 = i_mesli()
    _ = i_sesli()
    seq2 = i_mesli()
    series = list(set(seq1))
    ans = 0
    for num in seq2:
        if binary_search(num, series) is not None:
            ans += 1

    print(ans)
    sys.exit()


def binary_search(key, series):
    if len(series) == 0:
        return None

    if len(series) == 1:
        if key not in series:
            return None
        else:
            return 0

    left = 0
    right = len(series)

    mid = (left + right) // 2
    if series[mid] == key:
        return mid
    elif key < series[mid]:
        return binary_search(key, series[:mid])

    else:
        next_search = binary_search(key, series[mid:])
        if next_search is None:
            return None
        else:
            return mid + next_search


if __name__ == "__main__":
    main()
