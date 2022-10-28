from ITP1._11.mycode import Dice


LABELS_ASSERT = [i for i in range(1, 6 + 1)]


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
