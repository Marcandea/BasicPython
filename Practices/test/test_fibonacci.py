from unittest import TestCase
from BasicPython.Practices.src.fibonacci import Fibonacci
class TestFibonacci (TestCase):
    def test_fi(self):
        # Arrange
        fibbi = Fibonacci()
        # Act
        result_actual = fibbi.fi(1, 2, 3)
        # Assert
        result_expected ="12358"
        self.assertEqual(result_expected, result_actual)

