"""Tests of ITP1/11

failed cases(test)

['S', 'E', 'E', 'S', 'S', 'W', 'S', 'N', 'E', 'W']: [4, 6, 2, 5, 1, 3]
"""

import random
from typing import List

from ITP1._11.mycode import Dice


LABELS_ASSERT = [i for i in range(1, 6 + 1)]
DIRECTIONS = ['N', 'S', 'E', 'W']


class TestRoll:
    """Tests of Dice.roll()."""
    def test_roll_nn(self):
        _d = Dice(LABELS_ASSERT)
        _d.roll('N')
        assert _d.labels[0] == 2, f'actual: {_d.labels[0]}'
        _d.roll('N')
        assert _d.labels[0] == 6, f'actual: {_d.labels[0]}'

    def test_roll_se(self):
        _d = Dice(LABELS_ASSERT)
        _d.roll('S')
        assert _d.labels[0] == 5, f'actual: {_d.labels[0]}'
        _d.roll('E')
        assert _d.labels[0] == 4, f'actual: {_d.labels[0]}'

    def test_roll_eeswn(self):
        _d = Dice(LABELS_ASSERT)
        _d.roll('E')
        assert _d.labels[0] == 4, f'actual: {_d.labels[0]}'
        _d.roll('E')
        assert _d.labels[0] == 6, f'actual: {_d.labels[0]}'
        _d.roll('S')
        assert _d.labels[0] == 5, f'actual: {_d.labels[0]}'
        _d.roll('W')
        assert _d.labels[0] == 4, f'actual: {_d.labels[0]}'
        _d.roll('N')
        assert _d.labels[0] == 6, f'actual: {_d.labels[0]}'

    def test_roll_w(self):
        _d = Dice(LABELS_ASSERT)
        _d.roll('W')
        assert _d.labels[0] == 3, f'actual: {_d.labels[0]}'


class TestEquality:
    """Tests of 11C."""
    def test_eq_spc1(self):
        direction_chars = ['S', 'E', 'E', 'S', 'S', 'W', 'S', 'N', 'E', 'W']
        dice_init = Dice(LABELS_ASSERT)
        dice_rolled = Dice(LABELS_ASSERT)
        for direction in direction_chars:
            dice_rolled.roll(direction)

        assert dice_init == dice_rolled, f'{direction_chars = }: {dice_rolled.labels} must be equal to {dice_init.labels}'

    def test_eq_random(self):
        case_num = 10
        directions = [make_random_directions() for _ in range(case_num)]
        for direction_chars in directions:
            dice_init = Dice(LABELS_ASSERT)
            dice_rolled = Dice(LABELS_ASSERT)
            for direction in direction_chars:
                dice_rolled.roll(direction)

            assert dice_init == dice_rolled, f'{direction_chars = }: {dice_rolled.labels} must be equal to {dice_init.labels}'


def make_random_directions(length: int = 10) -> List[str]:
    random_directions = []
    for _ in range(length):
        direction = random.choice(DIRECTIONS)
        random_directions.append(direction)

    return random_directions
