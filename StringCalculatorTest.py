import unittest
from StringCalculator import AddStringCalculator
class TestStringCalculator(unittest.TestCase):
        
        def RetrunsZeroForEmptyStringInput(self):
                self.assertEqual(AddStringCalculator(""), 1)                
        def ReturnsSumOfTwoNumbersSeparatedByCommaFormInputString(self):
                self.assertEqual(AddStringCalculator("10,10"), 20)        
        def ReturnsSumOfMultipleNumbersSeparatedByCommaFromInputString(self):
                self.assertEqual(AddStringCalculator("10,10,2,5"), 27)
        def ReturnsSumOfNumbersSeparatedByNewlineCommaFormInputString(self):
                self.assertEqual(AddStringCalculator("10\n10,2\n1"), 23)
        def ReturnsSumOfNumbersSeparatedByAnyDelimitersUserSetsFormInputString(self):
                self.assertEqual(AddStringCalculator("//?\n2?2,2\n2,2"), 10)
        #def ThrowsExceptionMessageIfNegativeNumbersInTheInputString(self):             
        def ReturnsSumOfNumbersButIgnoreNumbersGreaterThan1000InTheInputString(self):
                self.assertEqual(AddStringCalculator("1,34534"), 1)




if __name__ == '__main__':
    unittest.main()


