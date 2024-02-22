"""
8_C : Counting Characters

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_C

Result:
"""

import string
import sys


ALPHABETS = string.ascii_lowercase


def main():
    s_org = sys.stdin.readlines()
    s = ''.join(s_org).lower()
    counts = {alphabet: 0 for alphabet in ALPHABETS}
    for alphabet in s:
        if alphabet in ALPHABETS:
            counts[alphabet] += 1

    for alphabet, num in counts.items():
        print(f'{alphabet} : {num}')


if __name__ == '__main__':
    main()
