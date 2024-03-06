"""ALDS1_3_C < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_3_C

Result: TLE
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesls = lambda: list(input())
i_memls = lambda n: [i_mesls() for _ in range(n)]


def main():
    n = i_sesli()
    commands = i_memls(n)
    ret = []
    for command in commands:
        operation = command[0]
        if operation == "insert":
            ret.insert(0, command[1])
        elif operation == "delete":
            if command[1] in ret:
                ret.remove(command[1])
        elif operation == "deleteFirst":
            ret = ret[1:]
        elif operation == "deleteLast":
            ret.pop()

    print(*ret)
    sys.exit()


if __name__ == "__main__":
    main()
