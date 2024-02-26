"""ALDS1_4_B < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_4_B

Run #2991887 < bal4u < Solutions | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/solutions/problem/ALDS1_4_B/review/2991887/bal4u/Python3

Result: AC
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    _ = i_sesli()
    set1 = set(i_mesli())
    _ = i_sesli()
    set2 = set(i_mesli())
    print(len(set1 & set2))
    sys.exit()


if __name__ == "__main__":
    main()
