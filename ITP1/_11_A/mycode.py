"""
11_A : Dice I

https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_11_A

Result:
"""

import pkg_resources
if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic

import sys


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesls = lambda: str(input()[0])
i_mesli = lambda: list(map(int, input()))

INF = float('inf')


def main():
    # test_roll()
    # sys.exit()
    labels = i_mesli()
    orders = list(i_sesls())
    dice = Dice(labels)
    for order in orders:
        dice.roll(order)

    print(f'{dice.labels[0]}')


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

    def roll(self, direction):
        current_labels = self.labels
        self.labels = [current_labels[i - 1] for i in self._rolled_map[direction]]
        return self


def test_roll():
    labels_assert = [i for i in range(1, 6 + 1)]

    _d = Dice(labels_assert)
    _d.roll('N')
    assert _d.labels[0] == 2, f'actual: {_d.labels[0]}'
    _d.roll('N')
    assert _d.labels[0] == 6, f'actual: {_d.labels[0]}'

    _d = Dice(labels_assert)
    assert _d.roll('S').labels[0] == 5
    _d.roll('E')
    assert _d.labels[0] == 4, f'actual: {_d.labels[0]}'

    _d = Dice(labels_assert)
    assert _d.roll('E').labels[0] == 4
    _d.roll('E')
    assert _d.labels[0] == 6, f'actual: {_d.labels[0]}'
    _d.roll('S')
    assert _d.labels[0] == 5, f'actual: {_d.labels[0]}'
    _d.roll('W')
    assert _d.labels[0] == 4, f'actual: {_d.labels[0]}'
    _d.roll('N')
    assert _d.labels[0] == 6, f'actual: {_d.labels[0]}'

    _d = Dice(labels_assert)
    assert _d.roll('W').labels[0] == 3


if __name__ == '__main__':
    main()
