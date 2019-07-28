from unittest import TestCase
from src.strong import Strong


class TestStrong(TestCase):
    def test_noNtrong(self):
        # Arranque
        st = Strong()
        # Assert
        result = st.strongNumber(454)
        # Assert
        result_expected = "No Strong"
        self.assertEqual(result_expected, result)

    def test_Strong(self):
        # Arranque
        st = Strong()
        # Assert
        result = st.strongNumber(145)
        # Assert
        result_expected = "Strong"
        self.assertEqual(result_expected, result)

    def test_strong_1_strong(self):
        # Arranque
        st = Strong()
        # Assert
        result = st.strongNumber(1)
        # Assert
        result_expected = "Strong"
        self.assertEqual(result_expected, result)

    def test_strong_2_strong(self):
        # Arranque
        st = Strong()
        # Assert
        result = st.strongNumber(1)
        # Assert
        result_expected = "Strong"
        self.assertEqual(result_expected, result)

    def test_strong_123_strong(self):
        # Arranque
        st = Strong()
        # Assert
        result = st.strongNumber(123)
        # Assert
        result_expected = "No Strong"
        self.assertEqual(result_expected, result)

    def test_strong_negative_number(self):
        # Arranque
        st = Strong()
        # Assert
        result = st.strongNumber(123)
        # Assert
        result_expected = "Negative Number"
        self.assertEqual(result_expected, result)

    def test_strong_zero_number_strong(self):
        # Arranque
        st = Strong()
        # Assert
        result = st.strongNumber(0)
        # Assert
        result_expected = "No Strong"
        self.assertEqual(result_expected, result)