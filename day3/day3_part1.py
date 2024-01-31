import re
import pytest 

def find_numbers(input_string):
    # Use regular expression to find all numbers
    matches = re.finditer(r'\d+', input_string)

    # Collect positions and numbers
    result = [(match) for match in matches]

    return result

def test_find_numbers():
    result = find_numbers("467..114..")
    assert len(result) == 2
    assert result[0].start() == 0
    assert result[0].end() == 3
    assert result[0].group() == "467"
    assert result[1].start() == 5
    assert result[1].end() == 8
    assert result[1].group() == "114"
    result = find_numbers("...*......")
    assert len(result) == 0

def find_special_char_indices(input_string):
    special_char_indices = []

    for i, char in enumerate(input_string):
        if not char.isalnum() and char != '.':
            special_char_indices.append(i)

    return special_char_indices

def test_find_special_char_indices():
    result = find_special_char_indices("467..114..")
    assert len(result) == 0
    result = find_special_char_indices("...*......")
    assert len(result) == 1
    assert result[0] == 3

def range_condition(number, specialCharPos):
    return specialCharPos >= max(number.start() - 1, 0) and specialCharPos <= number.end()

def test_range_condition():
    number = find_numbers("467...*...")
    assert range_condition(number[0], 0) == True
    assert range_condition(number[0], 3) == True
    assert range_condition(number[0], 4) == False
    assert range_condition(number[0], 10) == False
    number = find_numbers("..374.*...")
    assert range_condition(number[0], 0) == False
    assert range_condition(number[0], 1) == True
    assert range_condition(number[0], 2) == True
    assert range_condition(number[0], 3) == True
    assert range_condition(number[0], 4) == True
    assert range_condition(number[0], 5) == True
    assert range_condition(number[0], 6) == False
    assert range_condition(number[0], 7) == False


def special_char_connecting(number, prevLineSpecialCharIndices, currentLineSpecialCharIndices, nextLineSpecialCharIndices):
    connecting = False
    for specialCharPos in prevLineSpecialCharIndices:
        if range_condition(number, specialCharPos):
            connecting = True
    for specialCharPos in currentLineSpecialCharIndices:
        if range_condition(number, specialCharPos):
            connecting = True
    for specialCharPos in nextLineSpecialCharIndices:
        if range_condition(number, specialCharPos):
            connecting = True
    return connecting

def test_special_char_connecting():
    number = find_numbers("467...*...")
    assert special_char_connecting(number[0], [], [], []) == False
    assert special_char_connecting(number[0], [0], [], []) == True
    assert special_char_connecting(number[0], [], [3], []) == True
    assert special_char_connecting(number[0], [], [], [4]) == False
    assert special_char_connecting(number[0], [0], [3], []) == True
    assert special_char_connecting(number[0], [0], [], [4]) == True
    assert special_char_connecting(number[0], [], [3], [4]) == True
    assert special_char_connecting(number[0], [0], [3], [4]) == True
    assert special_char_connecting(number[0], [0], [3], [5]) == True
    assert special_char_connecting(number[0], [0], [3], [6]) == True
    assert special_char_connecting(number[0], [5], [4], [7]) == False
    assert special_char_connecting(number[0], [5], [4], [8]) == False
    assert special_char_connecting(number[0], [5], [4], [9]) == False
    assert special_char_connecting(number[0], [6], [5], [10]) == False

# Open the file in read mode
with open('day3/input_day3.txt', 'r') as file:

    sum = 0
    lineNr = 0
    currentLine = ""
    nextLine = ""
    prevLineSpecialCharIndices = []
    currentLineSpecialCharIndices = []
    nextLineSpecialCharIndices = []

    # Iterate over each line in the file
    for line in file:

        currentLine = nextLine
        nextLine = line.strip()
        # print(currentLine) 

        prevLineSpecialCharIndices = currentLineSpecialCharIndices
        currentLineSpecialCharIndices = nextLineSpecialCharIndices
        nextLineSpecialCharIndices = find_special_char_indices(nextLine)

        numbers = find_numbers(currentLine)
        # print("numbers: ", numbers)

        for number in numbers:
            # print("number: ", number, ", start: ", number.start(), ", end: ", number.end(), ", group: ", number.group())           
            if special_char_connecting(number, prevLineSpecialCharIndices, currentLineSpecialCharIndices, nextLineSpecialCharIndices):
                sum += int(number.group())

        lineNr += 1
    
    print("sum: ", sum)



        
