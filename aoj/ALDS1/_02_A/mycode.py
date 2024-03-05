"""バブルソート
ALDS1_2_A < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_2_A

@TODO: Implement
Result: WA
"""

import sys
from copy import deepcopy

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    _ = i_sesli()
    numbers = i_mesli()
    # print(numbers)
    print(*bubble_sort(numbers))
    print(count_op_bubble_sort(numbers))
    sys.exit()


def bubble_sort(numbers):
    seq = deepcopy(numbers)
    size = len(numbers)
    exists_left = True
    while exists_left:
        exists_left = False
        for i in range(size - 1, 0, -1):
            if seq[i] < seq[i - 1]:
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
                exists_left = True
    return seq


def count_op_bubble_sort(numbers):
    ret = 0
    seq = deepcopy(numbers)
    size = len(numbers)
    exists_left = True
    while exists_left:
        exists_left = False
        for i in range(size - 1, 0, -1):
            if seq[i] < seq[i - 1]:
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
                ret += 1
                exists_left = True
    return ret


if __name__ == "__main__":
    main()
