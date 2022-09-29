"""
Official House

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/6/ITP1_6_C

Result: 未提出
"""

import sys

import icecream


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_mesls = lambda: list(input())
i_memls = lambda n: [i_mesls() for _ in range(n)]


DELIMITER = '####################'
ROOMS_PER_FLOOR = 10
FLOOR_NUM_PER_BUILDING = 3
BUILDING_NUM = 4

def main():
    n = i_sesli()
    moved_in_residents = i_memls(n)

    # 初期状態(全て 0)の `residents` 定義
    residents_per_floor = {str(i): 0 for i in range(1, ROOMS_PER_FLOOR + 1)}
    residents_per_building = {str(i): residents_per_floor for i in range(1, FLOOR_NUM_PER_BUILDING + 1)}
    residents = {str(i): residents_per_building for i in range(1, BUILDING_NUM + 1)}

    for moved_in_resident in moved_in_residents:
        b = moved_in_resident[0]
        f = moved_in_resident[1]
        r = moved_in_resident[2]
        v = int(moved_in_resident[3])
        # icecream.ic(residents['1']['1']['3'])  # ic| residents['1']['1']['3']: 0
        # icecream.ic(residents['2']['1']['3'])  # ic| residents['2']['1']['3']: 0
        residents[b][f][r] = v
        # icecream.ic(residents['1']['1']['3'])  # ic| residents['1']['1']['3']: 8
        # icecream.ic(residents['2']['1']['3'])  # ic| residents['2']['1']['3']: 8
        # icecream.ic(residents)
        # sys.exit()

    # sys.exit()
    # icecream.ic(residents)
    residents_for_print = []
    for building_num, residents_per_building in residents.items():
        icecream.ic(building_num, residents_per_building)
        for _, residents_per_floor in residents_per_building.items():
            line_for_print = ' '.join(residents_per_floor)
            residents_for_print.append(line_for_print)
        if building_num != str(BUILDING_NUM):
            residents_for_print.append(DELIMITER)

    for l in residents_for_print:
        print(l)


if __name__ == '__main__':
    main()
