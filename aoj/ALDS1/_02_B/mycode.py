"""ALDS1_2_B < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_2_B

Result: AC
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    _ = i_sesli()
    seq = i_mesli()
    ret = selection_sort(seq)
    print(*ret["seq"])
    print(ret["count"])
    sys.exit()


def selection_sort(seq):
    count = 0
    size = len(seq)
    for i, num in enumerate(seq):
        min_index = i
        for j in range(i, size):
            if seq[j] < seq[min_index]:
                min_index = j
        seq_i = seq[i]
        seq_min_index = seq[min_index]
        seq[i] = seq_min_index
        seq[min_index] = seq_i
        if seq_i != seq_min_index:
            count += 1

    return {"seq": seq, "count": count}


if __name__ == "__main__":
    main()
