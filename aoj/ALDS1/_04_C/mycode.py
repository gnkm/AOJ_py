"""ALDS1_4_C < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_4_C

Result: AC
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesls = lambda: list(input())
i_memls = lambda n: [i_mesls() for _ in range(n)]


def main():
    N = i_sesli()
    queries = i_memls(N)
    dictionary = set()
    for query in queries:
        operation = query[0]
        query_string = query[1]
        if operation == "insert":
            dictionary.add(query_string)
        elif operation == "find":
            if query_string in dictionary:
                print("yes")
            else:
                print("no")
    sys.exit()


if __name__ == "__main__":
    main()
