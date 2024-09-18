import unittest
from StringCalculator import StringCalculator
class TestStringCalculator(unittest.TestCase):
        
        def RetrunsZeroForEmptyStringInput(self):
                self.assertEqual(StringCalculator(""), 0)                
        def ReturnsSumOfTwoNumbersSeparatedByCommaFormInputString(self):
                self.assertEqual(StringCalculator("10,10"), 20)        
        def ReturnsSumOfMultipleNumbersSeparatedByCommaFromInputString(self):
                self.assertEqual(StringCalculator("10,10,2,5"), 27)
        def ReturnsSumOfNumbersSeparatedByNewlineCommaFormInputString(self):
                self.assertEqual(StringCalculator("10\n10,2\n1"), 23)
        def ReturnsSumOfNumbersSeparatedByAnyDelimitersUserSetsFormInputString(self):
                self.assertEqual(StringCalculator("//?\n2?2,2\n2,2"), 10)
        #def ThrowsExceptionMessageIfNegativeNumbersInTheInputString(self):     
        def ReturnsSumOfNumbersButIgnoreNumbersGreaterThan1000InTheInputString(self):
                self.assertEqual(StringCalculator("1,34534"), 1)




if __name__ == '__main__':
    unittest.main()


