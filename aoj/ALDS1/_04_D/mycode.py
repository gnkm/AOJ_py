"""ALDS1_4_D < Lesson < Courses | Aizu Online Judge
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_4_D

※ ベルトコンベアから流れてきた連続する 0 個以上の荷物を載せられることに注意

@TODO: Implement
Result: WA
"""

import math
import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])
i_mesli = lambda: list(map(int, input()))


def main():
    luggage_num, truck_num = i_mesli()
    weights = []
    for _ in range(luggage_num):
        weight = i_sesli()
        weights.append(weight)

    ans = get_ideal_maximum_loading_capacity(weights, truck_num)
    tmp_weight_sum = 0
    tmp_truck_sum = 0
    for weight in weights:
        pass

    print(ans)
    sys.exit()


def get_ideal_maximum_loading_capacity(weights, truck_num):
    """順序を考慮しない場合の最大積載量の最小値を返す。"""
    weight_per_truck_min = math.ceil(sum(weights) / truck_num)
    weight_max = max(weights)
    ret = max(weight_per_truck_min, weight_max)
    return ret


if __name__ == "__main__":
    main()
