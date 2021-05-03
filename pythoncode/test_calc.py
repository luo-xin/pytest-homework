import pytest

from pythoncode.calculator import Calculator


class Test_Calc:
    def setup_class(self):
        self.calc = Calculator()
        print('开始计算')
    def teardown_calss(self):
        print('结束计算')

    @pytest.mark.parametrize('a, b, expect', [
        (10, 20, 30), (-1, -3, -4), (11.5, 12.5, 24)
    ], ids=['1', '2', '3']
                             )
    def test_add(self, a, b, expect):
        assert self.calc.add(a, b) == expect

    @pytest.mark.parametrize('a, b, expect', [
        (20, 10, 10), (-5, -3, -2), (12.5, 11.5, 1)
    ], ids=['4', '5', '6']
                             )
    def test_sub(self, a, b, expect):
        assert self.calc.sub(a, b) == expect

    @pytest.mark.parametrize('a, b, expect', [
        (4, 5, 20), (1, 5, 5), (1, 1, 1)
    ], ids=['7', '8', '9']
                             )
    def test_mul(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @pytest.mark.parametrize('a, b, expect', [
        (20, 4, 5), (10, 5, 2), (3, 1, 3)
    ], ids=['10', '11', '12']
                             )
    def test_div(self, a, b, expect):
        assert self.calc.div(a, b) == expect