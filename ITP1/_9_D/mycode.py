"""
9_D : Transformation

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_D

Result:

Test:
- [x]  : 01
- [x]  : 02
- [x]  : 03(test print)
- [x]  : 04(test reverse)
- [x]  : 05(test reverse)
- [x]  : 06(test replace)
- [x]  : 07(test replace)
"""

import pkg_resources
if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_sesls = lambda: str(input()[0])
i_mesls = lambda: list(input())
i_memls = lambda n: [i_mesls() for _ in range(n)]


def main():
    string = i_sesls()
    order_num = i_sesli()
    orders = i_memls(order_num)

    for order in orders:
        order_name = order[0]
        first_arg = int(order[1])
        snd_arg = int(order[2])

        if order_name == 'print':
            print(string[first_arg:snd_arg + 1])
        elif order_name == 'reverse':
            head = string[:first_arg]

            if first_arg == 0:
                mid = string[snd_arg::-1]
            else:
                mid = string[snd_arg:first_arg - 1:-1]

            if snd_arg == len(string):
                tail = ''
            else:
                tail = string[snd_arg + 1:]

            string = head + mid + tail
        elif order_name == 'replace':
            replaced_str = order[3]
            string = string[:first_arg] + replaced_str + string[snd_arg + 1:]


if __name__ == '__main__':
    main()
