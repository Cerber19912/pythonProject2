import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 15, 20) == 35

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1,) == 3

    def test_zero_divizion(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_substraction_success(self):
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_division_success(self):
        assert self.calc.division(self, 15, 5) == 3