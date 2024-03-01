"""素数
ALDS1_1_C < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_1_C

Result: AC
"""

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_semli = lambda n: [i_sesli() for _ in range(n)]


def main():
    n = i_sesli()
    numbers = i_semli(n)
    print(sum([is_prime(n) for n in numbers]))
    sys.exit()


def is_prime(number):
    max_num = int(pow(number, 1 / 2))
    for num in range(2, max_num + 1):
        if number % num == 0:
            return False
    return True


if __name__ == "__main__":
    main()
