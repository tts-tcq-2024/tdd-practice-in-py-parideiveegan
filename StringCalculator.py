def check_for_new_delimiter(inputstring, separators):
    if inputstring[0]!='/':
        return separators
    delimiter = ''
    index = 2
    while inputstring[index] !='\n':
        delimiter +=inputstring[index]
        index +=1
    separators.append(delimiter)
    return [separators,index]

def check_append(inputstring, index):
    number_found = 0
    delimiter = ''
    while not number_found:
        if inputstring[index]

def get_numbers(inputstring, separators):
    
    refactored_inputstring = inputstring
    delimiter = ''
    number = ''
    index = 0
    result = []
    numbers = []
    while index <= len(inputstring)-1:
        result = check_append(inputstring,index)
        index = result[0]
        number +=inputstring[index]
        if result[1]:
            numbers.append(number)
            number = ''

def AddStringCalculator(inputstring):
   if not inputstring:
      return 0
   separators = ['\n',',']
   changes = check_for_new_delimiter(inputstring,separators)
   separators = changes[0]
   inputstring = inputstring[(changes[1]+1):]

   numbers = get_numbers(inputstring, separators)
   
