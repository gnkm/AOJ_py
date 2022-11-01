"""
11 : Dice

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_11_A
https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_11_B
https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_11_C
https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_11_D

ラベルの定義

     ---
    | 1 |
 --- --- --- ---
| 4 | 2 | 3 | 5 |
 --- --- --- ---
    | 6 |
     ---

Result:

- 11A: AC
- 11B: AC
- 11C: WA(#9)
"""

import pkg_resources
if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])
i_sesls = lambda: str(input()[0])
i_memli = lambda n: [i_mesli() for _ in range(n)]
i_mesli = lambda: list(map(int, input()))

DIRECTIONS = ['N', 'S', 'E', 'W']


def main():
    # solve11a()
    # solve11b()
    solve11c()


def solve11a():
    labels = i_mesli()
    orders = list(i_sesls())
    dice = Dice(labels)
    for order in orders:
        dice.roll(order)

    print(f'{dice.labels[0]}')


def solve11b():
    labels = i_mesli()
    question_num = i_sesli()
    questions = i_memli(question_num)
    dice = Dice(labels)
    for q in questions:
        print(f'{dice.right_side_label(q[0], q[1])}')


def solve11c():
    """サイコロの同一判定
    """
    labels1 = i_mesli()
    labels2 = i_mesli()
    dice1 = Dice(labels1)
    dice2 = Dice(labels2)
    if dice1 == dice2:
        print('Yes')
    else:
        print('No')


class Dice():
    labels = []
    _rolled_map = {
        # N に転がすと、新しい 1 の面は旧 2 の面、新しい 2 の面は旧 6 の面 ... に変わることを意味する
        'N': [2, 6, 3, 4, 1, 5],
        'S': [5, 1, 3, 4, 6, 2],
        'E': [4, 2, 1, 6, 5, 3],
        'W': [3, 2, 6, 1, 5, 4],
    }

    def __init__(self, labels):
        self.labels = labels

    def __eq__(self, another: object) -> bool:
        """同一判定。

        N / S 方向に転がすと、1, 2, 6, 5 で巡回する。(3, 4 が固定面) ... ring_34
        E / W 方向に転がすと、1, 4, 6, 3 で巡回する。(2, 5 が固定面) ... ring_25
        ある方向に転がした後、もう一方の方向に転がすと、 で巡回する。(1, 6 が固定面) ... ring_16
        したがって同一条件は下記のいずれかである。

        - 条件 1: 下記 2 項を満たすこと
          - ring_34 の順序(clockwise / counterclockwise)が一致
          - 3 の面が一致
        - 条件 2: 下記 2 項を満たすこと
          - ring_34 の順序(clockwise / counterclockwise)が逆
          - 一方の 3 の面と、もう一方の 4 の面が一致
        - 条件 3: 下記 2 項を満たすこと
          - ring_25 の順序(clockwise / counterclockwise)が一致
          - 2 の面が一致
        - 条件 4: 下記 2 項を満たすこと
          - ring_25 の順序(clockwise / counterclockwise)が逆
          - 一方の 2 の面と、もう一方の 5 の面が一致
        - 条件 5: 下記 2 項を満たすこと
          - ring_25 と ring_34 の順序(clockwise / counterclockwise)が一致
          - ring_25 の 2 の面と ring_34 の 3 の面が一致
        - 条件 6: 下記 2 項を満たすこと
          - ring_25 と ring_34 の順序(clockwise / counterclockwise)が逆
          - ring_25 の 2 の面と ring_34 の 4 の面が一致

        Args:
            another (object): _description_

        Returns:
            bool: _description_
        """
        # ----- 条件 1 -----
        ring_34_myself = set([
            (self.labels[0], self.labels[1]),
            (self.labels[1], self.labels[5]),
            (self.labels[5], self.labels[4]),
            (self.labels[4], self.labels[0]),
        ])

        ring_34_another_clockwise = set([
            (another.labels[0], another.labels[1]),
            (another.labels[1], another.labels[5]),
            (another.labels[5], another.labels[4]),
            (another.labels[4], another.labels[0]),
        ])

        if all([
            ring_34_myself == ring_34_another_clockwise,
            self.labels[2] == another.labels[2],
            self.labels[3] == another.labels[3],
        ]):
            return True

        # ----- 条件 2 -----
        ring_34_another_counterclockwise = set([(t[1], t[0]) for t in list(ring_34_another_clockwise)])

        if all([
            ring_34_myself == ring_34_another_counterclockwise,
            self.labels[2] == another.labels[3],
            self.labels[3] == another.labels[2],
        ]):
            return True

        # ----- 条件 3 -----
        ring_25_myself = set([
            (self.labels[0], self.labels[3]),
            (self.labels[3], self.labels[5]),
            (self.labels[5], self.labels[2]),
            (self.labels[2], self.labels[0]),
        ])

        ring_25_another_clockwise = set([
            (another.labels[0], another.labels[3]),
            (another.labels[3], another.labels[5]),
            (another.labels[5], another.labels[2]),
            (another.labels[2], another.labels[0]),
        ])

        if all([
            ring_25_myself == ring_25_another_clockwise,
            self.labels[1] == another.labels[1],
            self.labels[4] == another.labels[4],
        ]):
            return True

        # ----- 条件 4 -----
        ring_25_another_counterclockwise = set([(t[1], t[0]) for t in list(ring_25_another_clockwise)])

        if all([
            ring_25_myself == ring_25_another_counterclockwise,
            self.labels[1] == another.labels[4],
            self.labels[4] == another.labels[1],
        ]):
            return True

        # ----- 条件 5 -----
        if all([
            ring_25_myself == ring_34_another_clockwise,
            self.labels[1] == another.labels[2],
        ]):
            return True

        if all([
            ring_34_myself == ring_25_another_clockwise,
            self.labels[2] == another.labels[1],
        ]):
            return True

        # ----- 条件 6 -----
        if all([
            ring_25_myself == ring_34_another_counterclockwise,
            self.labels[1] == another.labels[3],
        ]):
            return True

        if all([
            ring_34_myself == ring_25_another_counterclockwise,
            self.labels[3] == another.labels[1],
        ]):
            return True

        return False

    def roll(self, direction):
        current_labels = self.labels
        self.labels = [current_labels[i - 1] for i in self._rolled_map[direction]]
        return self

    def right_side_label(self, top_side_label, following_side_label):
        for i, label in enumerate(self.labels):
            if top_side_label == label:
                top_side = i + 1
            if following_side_label == label:
                following_side = i + 1
        pair = (top_side, following_side)
        # 1
        ret1 = [(4, 2), (2, 3), (3, 5), (5, 4)]
        if pair in ret1:
            return self.labels[0]
        # 6
        ret6 = [(e[1], e[0]) for e in ret1]
        if pair in ret6:
            return self.labels[5]
        # 2
        ret2 = [(4, 6), (6, 3), (3, 1), (1, 4)]
        if pair in ret2:
            return self.labels[1]
        # 5
        ret5 = [(e[1], e[0]) for e in ret2]
        if pair in ret5:
            return self.labels[4]
        # 3
        ret3 = [(1, 2), (2, 6), (6, 5), (5, 1)]
        if pair in ret3:
            return self.labels[2]
        # 4
        return self.labels[3]


if __name__ == '__main__':
    main()
