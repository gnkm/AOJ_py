"""
挿入ソート

https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_A

Result: AC
"""

try:
    import icecream

    debug = icecream.ic
except Exception:
    debug = print

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    N = i_sesli()
    numbers = i_mesli()
    insertion_sort(numbers, N)
    sys.exit()


def insertion_sort(numbers, N):
    print(*numbers)
    for i, num in enumerate(numbers):
        if i == 0:
            continue
        j = i - 1
        while j >= 0 and numbers[j] > num:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = num
        print(*numbers)


if __name__ == "__main__":
    main()
