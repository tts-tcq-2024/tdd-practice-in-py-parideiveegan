import unittest
from StringCalculator import AddStringCalculator
class TestStringCalculator(unittest.TestCase):
        
        def test_RetrunsZeroForEmptyStringInput(self):
                self.assertEqual(AddStringCalculator(""), 0)                
        def test_ReturnsSumOfTwoNumbersSeparatedByCommaFormInputString(self):
                self.assertEqual(AddStringCalculator("10,10"), 20)        
        def test_ReturnsSumOfMultipleNumbersSeparatedByCommaFromInputString(self):
                self.assertEqual(AddStringCalculator("10,10,2,5"), 27)
        def test_ReturnsSumOfNumbersSeparatedByNewlineCommaFormInputString(self):
                self.assertEqual(AddStringCalculator("10\n10,2\n1"), 23)
        def test_ReturnsSumOfNumbersSeparatedByAnyDelimitersUserSetsFormInputString(self):
                self.assertEqual(AddStringCalculator("//?\n2?2,2\n2,2"), 10)
        def test_ReturnsSumOfNumbersButIgnoreNumbersGreaterThan1000InTheInputString(self):
                self.assertEqual(AddStringCalculator("1,34534"), 1)
        def test_ThrowsExceptionMessageIfNegativeNumbersInTheInputString(self):
                self.assertRaises(Exception):
                        AddStringCalculator("-1,6,-22")





if __name__ == '__main__':
    unittest.main()


