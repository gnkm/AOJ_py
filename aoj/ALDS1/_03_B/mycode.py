"""ALDS1_3_B < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_3_B

Result: $(result)
"""

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: list(map(int, input()))
i_mesls = lambda: list(input())
i_memls = lambda n: [i_mesls() for _ in range(n)]


def main():
    n, q = i_mesli()
    queries_org = i_memls(n)
    queries = [[row[0], int(row[1])] for row in queries_org]
    _deque = deque(queries)
    answer = []
    t = 0
    while len(_deque) > 0:
        query = _deque.popleft()
        process_name = query[0]
        process_time = query[1]
        if process_time <= q:
            t += process_time
            answer.append([process_name, t])
        else:
            t += q
            _deque.append([process_name, process_time - q])

    for row in answer:
        print(row[0], row[1])

    sys.exit()


if __name__ == "__main__":
    main()
