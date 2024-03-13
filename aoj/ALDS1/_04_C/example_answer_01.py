"""ALDS1_4_C < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/solutions/problem/ALDS1_4_C/review/6647260/naoto172/Python3

Result: AC
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])


def main():
    N = i_sesli()
    dictionary = set()
    for _ in range(N):
        command, word = map(str, input())
        if command == "insert":
            dictionary.add(word)
        elif command == "find":
            if word in dictionary:
                print("yes")
            else:
                print("no")

    sys.exit()


if __name__ == "__main__":
    main()
