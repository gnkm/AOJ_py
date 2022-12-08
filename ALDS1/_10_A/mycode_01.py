"""
10_A : Fibonacci Number

https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_10_A

Result: AC

Dynamic Programming 使用。
"""

# for debugging
import icecream
debug = icecream.ic

# submit the following code
import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    number = int(input()[0])
    print(nth_fibonacci(number))
    sys.exit()


def nth_fibonacci(number):
    dp = {0: 1, 1: 1}
    if number <= len(dp) - 1:
        return dp[number]

    for i in range(2, number + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[number]


if __name__ == '__main__':
    main()
