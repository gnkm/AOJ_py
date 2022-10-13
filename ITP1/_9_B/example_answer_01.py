"""
9_B : Shuffle

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_B

https://onlinejudge.u-aizu.ac.jp/solutions/problem/ITP1_9_B/review/4956815/mohejin/Python3
"""

while True:
    s=input()
    if s=="-":break
    m=int(input())
    for i in range(m):
        h=int(input())
        le=s[0:h]
        ri=s[h:]
        s=ri+le
    print(s)
