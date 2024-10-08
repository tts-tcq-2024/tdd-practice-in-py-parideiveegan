def check_for_new_delimiter(inputstring, separators):
    if inputstring[0]!='/':
        return separators
    delimiter = ''
    index = 2
    while inputstring[index] !='\n':
        delimiter +=inputstring[index]
        index +=1
    separators.append(delimiter)
    delimiter = separators[-1]+'-1'
    separators.append(delimiter)
    return separators
    
def get_digit_index(inputstring):
    index_list = []
    index = 0
    while index <= len(inputstring)-1:
        if 48<= ord(inputstring[index]) <= 57 :
            index_list.append(index)
        index +=1
    return index_list    

def check_delimiter(tail_pointer,head_pointer,separators,inputstring):
    delimiter_start = tail_pointer+1
    delimiter_end = head_pointer
    delimiter = inputstring[delimiter_start:delimiter_end]
    return delimiter not in separators
               
def get_numbers(inputstring, separators):
    digit_index = get_digit_index(inputstring)
    head_pointer = 1
    tail_pointer = 0
    digit = [digit_index[0]]
    numbers = []
    while head_pointer <= len(digit_index)-1:
        if check_delimiter(digit_index[tail_pointer],digit_index[head_pointer],separators,inputstring):
            digit.append(digit_index[head_pointer])
            tail_pointer = head_pointer
            head_pointer +=1
            continue
        numbers.append(digit)
        tail_pointer = head_pointer
        digit = [digit_index[tail_pointer]]
        head_pointer +=1
        
    numbers.append(digit)    
    return numbers

def ConvertToNumber(number,inputstring):
    converted_number = 0
    for index in number:
        value = ord(inputstring[index]) - ord('0')
        converted_number = value + (converted_number*10)
    return converted_number

def check_negative(numbers,inputstring):
    index = 0
    negative_numbers = []
    number = []
    while index <= len(numbers)-1:        
        number = numbers[index]
        minus_index = inputstring[number[0]-1]
        if minus_index == '-':
            negative_numbers.append(number)
        index +=1
    return negative_numbers
    
def check_exception(negative_numbers,inputstring):
    
    if negative_numbers:
        statement = "negatives not allowed : "
        index = 0
        number = 0
        while index<= len(negative_numbers)-1:
            number = ConvertToNumber(negative_numbers[index],inputstring)
            statement += (" -"+str(number))
            index +=1
            
        raise Exception(statement)
    
def get_sum(numbers,inputstring):
    total_sum = 0
    index = 0
    negative_numbers = check_negative(numbers,inputstring)
    check_exception(negative_numbers,inputstring)
    while index <= len(numbers)-1:        
        number = numbers[index]        
        integer = ConvertToNumber(number,inputstring)
        if integer <= 1000:
            total_sum += ConvertToNumber(number,inputstring)
        index+=1
    return total_sum

def AddStringCalculator(inputstring):
    if not inputstring:
      return 0
    separators = ['\n',',',',-','\n-']
    separators = check_for_new_delimiter(inputstring,separators)
    numbers = get_numbers(inputstring, separators)
    total_sum = get_sum(numbers,inputstring)
    return (total_sum)
