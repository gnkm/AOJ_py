"""
https://onlinejudge.u-aizu.ac.jp/solutions/problem/ITP1_9_D/review/3216251/jakenu0x5e/Python3
"""

import pkg_resources
if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic

import sys

s1 = 'abcde'
s2 = reversed(s1)
# print(s2)  # => <reversed object at 0x1030fa5b0>
print(*s2, sep='')  # => 'edcba'
# print(*s2[0:2], sep='')  # => TypeError: 'reversed' object is not subscriptable

sys.exit()

s = list(input())
for i in range(int(input())):
    cmd, a, b, *c = input().split()
    a = int(a); b = int(b)
    if cmd == "print":
        print(*s[a:b+1], sep='')
    elif cmd == "reverse":
        s[a:b+1] = reversed(s[a:b+1])
    else:
        s[a:b+1] = c[0]
