"""
ALDS1_5_A < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_5_A

Result: WA
"""

try:
    import icecream

    debug = icecream.ic
except Exception:
    debug = print

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_semli = lambda n: [i_sesli() for _ in range(n)]
i_mesli = lambda: list(map(int, input()))


def main():
    n = i_sesli()
    A = i_mesli()
    q = i_sesli()
    questions = i_mesli()
    enables = []
    disables = []
    for q_num in questions:
        is_enable = False
        if q_num in enables:
            is_enable = True
        elif q_num in disables:
            pass
        else:
            for i, num_i in enumerate(A):
                if i == len(A) - 1:
                    break
                for num_j in A[i + 1 :]:
                    summation = num_i + num_j
                    if summation == q_num:
                        is_enable = True
                        enables.append(q_num)
                    else:
                        disables.append(q_num)

        if is_enable:
            print("yes")
        else:
            print("no")
    sys.exit()


if __name__ == "__main__":
    main()
