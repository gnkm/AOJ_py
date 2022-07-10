from ALDS1._1_D import (
    mycode,
    example_answer_01,
)


class TestMyCode:
    def test_case1(self):
        assert mycode.main([5, 3, 1, 3, 4, 3]) == 3

    def test_case2(self):
        assert mycode.main([4, 3, 2]) == -1

    def test_case3(self):
        assert mycode.main([1, 1]) == 0

    def test_case4(self):
        assert mycode.main([100, 95, 85, 90]) == 5

    def test_case5(self):
        assert mycode.main([600, 250, 450, 550, 300, 900, 450, 800, 900, 800, 450, 150, 300, 500, 600, 500, 500, 600, 550, 900]) == 750


class TestEx01:
    def test_case1(self):
        assert example_answer_01.main([5, 3, 1, 3, 4, 3]) == 3

    def test_case2(self):
        assert example_answer_01.main([4, 3, 2]) == -1

    def test_case3(self):
        assert example_answer_01.main([1, 1]) == 0

    def test_case4(self):
        assert example_answer_01.main([100, 95, 85, 90]) == 5

    def test_case5(self):
        assert example_answer_01.main([600, 250, 450, 550, 300, 900, 450, 800, 900, 800, 450, 150, 300, 500, 600, 500, 500, 600, 550, 900]) == 750
