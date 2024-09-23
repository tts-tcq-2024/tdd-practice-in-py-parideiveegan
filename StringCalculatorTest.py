import unittest
from StringCalculator import AddStringCalculator
class TestStringCalculator(unittest.TestCase):
        
        def Test_RetrunsZeroForEmptyStringInput(self):
                self.assertEqual(AddStringCalculator(""), 0)                
        def ReturnsSumOfTwoNumbersSeparatedByCommaFormInputString(self):
                self.assertEqual(AddStringCalculator("10,10"), 20)        
        def ReturnsSumOfMultipleNumbersSeparatedByCommaFromInputString(self):
                self.assertEqual(AddStringCalculator("10,10,2,5"), 27)
        def ReturnsSumOfNumbersSeparatedByNewlineCommaFormInputString(self):
                self.assertEqual(AddStringCalculator("10\n10,2\n1"), 23)
        def ReturnsSumOfNumbersSeparatedByAnyDelimitersUserSetsFormInputString(self):
                self.assertEqual(AddStringCalculator("//?\n2?2,2\n2,2"), 10)
        def ThrowsExceptionMessageIfNegativeNumbersInTheInputString(self):
                self.assertEqual(AddStringCalculator("-1,6,-22"),"negatives not allowed : -1,-22")
        def ReturnsSumOfNumbersButIgnoreNumbersGreaterThan1000InTheInputString(self):
                self.assertEqual(AddStringCalculator("1,34534"), 1)




if __name__ == '__main__':
    unittest.main()


