"""
8_C : Counting Characters

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_C
https://onlinejudge.u-aizu.ac.jp/solutions/problem/ITP1_8_C/review/3232451/kyuna/Python3
"""

import sys;s=sys.stdin.read().lower()
for c in map(chr,range(97,123)):print(c,':',s.count(c))
