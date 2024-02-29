"""ALDS1_4_B < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_4_B

Result: TLE
@TODO: Implement
"""

import sys
from copy import deepcopy
from typing import List, Union

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    _ = i_sesli()
    haystack = i_mesli()
    _ = i_sesli()
    needles = i_mesli()
    ans = 0
    for needle in needles:
        # print(f"{needle = }, {linear_search_with_guard(needle, haystack) = }")
        if linear_search_with_guard(needle, haystack) is not None:
            ans += 1

    print(ans)
    sys.exit()


def linear_search_with_guard(needle: int, haystack: List[int]) -> Union[int, None]:
    """`haystack` の中に `needle` を見つけたら、`haystack` のインデックスを返す。
    linear search で guard を使った書き方。

    Args:
        needle (int): 探す数
        haystack (List[int]): 数のリスト

    Returns:
        int: needle が存在する haystack のインデックス。なければ None.
    """
    i = 0
    _haystack = deepcopy(haystack)
    _haystack.append(needle)
    while _haystack[i] != needle:
        i += 1
    if i == len(_haystack) - 1:
        return None
    return i


if __name__ == "__main__":
    main()
