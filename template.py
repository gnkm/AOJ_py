import icecream, pprint  # for debugging
import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sli = lambda: list(map(int, input()))
i_slf = lambda: list(map(float, input()))
i_sls = lambda: list(input())
i_mli = lambda n: [i_sli() for _ in range(n)]
i_mlf = lambda n: [i_slf() for _ in range(n)]
i_mls = lambda n: [i_sls() for _ in range(n)]

sys.setrecursionlimit(1000000)

def main():
    pass

if __name__ == '__main__':
    main()
