from unittest import TestCase
from src.calculator import Calculator


class TestCalculator(TestCase):

    def test_sum(self):
            # Arrange
            calculator = Calculator()
            # Act
            result_actual = calculator.sum(1, 2)
            # Assert
            result_expected = 3
            self.assertEqual(result_expected, result_actual)

    def test_subtraction(self):
        # Arrange
        calculator = Calculator()
        # Act
        result_actual = calculator.subtraction(1, 2)
        # Assert
        result_expected = -1
        self.assertEqual(result_expected, result_actual)

    def test_multiplication(self):
        # Arrange
        calculator = Calculator()
        # Act
        result_actual = calculator.multiplication(1, 2)
        # Assert
        result_expected = 2
        self.assertEqual(result_expected, result_actual)

    def test_division(self):
        # Arrange
        calculator = Calculator()
        # Act
        result_actual = calculator.division(2, 2)
        # Assert
        result_expected = 1
        self.assertEqual(result_expected, result_actual)

    def test_division_first_number_0(self):
        # Arrange
        calculator = Calculator()
        # Act
        result_actual = calculator.division(0, 2)
        # Assert
        result_expected = 0
        self.assertEqual(result_expected, result_actual)

    def test_division_second_number_0(self):
        # Arrange
        calculator = Calculator()
        # Act
        result_actual = calculator.division(2, 0)
        # Assert
        result_expected = None
        self.assertEqual(result_expected, result_actual)

    def test_division_number_major(self):
        # Arrange
        calculator = Calculator()
        # Act
        result_actual = calculator.division(1, 3)
        # Assert
        result_expected = 0.3333333333333333
        self.assertEqual(result_expected, result_actual)
