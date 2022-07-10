from ALDS1._1_D import mycode


class TestProfit:
    def test_case1(self):
        assert mycode.main([5, 3, 1, 3, 4, 3]) == 3

    def test_case2(self):
        assert mycode.main([4, 3, 2]) == -1

    def test_case3(self):
        assert mycode.main([1, 1]) == 0
