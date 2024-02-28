"""ALDS1_4_B < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_4_B

Result: AC
"""

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    _ = i_sesli()
    seq1 = i_mesli()
    _ = i_sesli()
    seq2 = i_mesli()
    counter = Counter(set(seq1))
    ans = 0
    for num in seq2:
        ans += counter[num]

    print(ans)
    sys.exit()


if __name__ == "__main__":
    main()
