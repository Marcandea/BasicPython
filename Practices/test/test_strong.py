from unittest import TestCase
from BasicPython.Practices.src.strong import Strong
class TestStrong (TestCase):
    def test_noNtrong(self):
        #Arranque
        st = Strong()
        #Assert
        result=st.strongNumber(454)
        #Assert
        result_expected="No Strong"
        self.assertEqual(result_expected, result)

    def test_Strong(self):
        #Arranque
        st = Strong()
        #Assert
        result=st.strongNumber(145)
        #Assert
        result_expected="Strong"
        self.assertEqual(result_expected, result)