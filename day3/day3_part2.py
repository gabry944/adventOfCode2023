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

def numbers_connecting_star(starPlacement, prevLineNumbers, currentLineNumbers, nextLineNumbers):
    numbers = []
    for number in prevLineNumbers:
        if range_condition(number, starPlacement):
            numbers.append(number)
    for number in currentLineNumbers:
        if range_condition(number, starPlacement):
            numbers.append(number)
    for number in nextLineNumbers:
        if range_condition(number, starPlacement):
            numbers.append(number)
    return numbers

def test_numbers_connecting_star():
    prevLineNumbers =    find_numbers("467..114..")
    currentLineNumbers = find_numbers("...*......")
    nextLineNumbers =    find_numbers("..35..63..")

    result = numbers_connecting_star(0, prevLineNumbers, currentLineNumbers, nextLineNumbers)
    assert len(result) == 1
    assert int(result[0].group()) == 467

    result = numbers_connecting_star(1, prevLineNumbers, currentLineNumbers, nextLineNumbers)
    assert len(result) == 2
    assert int(result[0].group()) == 467
    assert int(result[1].group()) == 35

    result = numbers_connecting_star(2, prevLineNumbers, currentLineNumbers, nextLineNumbers)
    assert len(result) == 2
    assert int(result[0].group()) == 467
    assert int(result[1].group()) == 35

    result = numbers_connecting_star(3, prevLineNumbers, currentLineNumbers, nextLineNumbers)
    assert len(result) == 2
    assert int(result[0].group()) == 467
    assert int(result[1].group()) == 35

    result = numbers_connecting_star(9, prevLineNumbers, currentLineNumbers, nextLineNumbers)
    assert len(result) == 0

def find_stars(input_string):
    starPlacements = []
    for i, char in enumerate(input_string):
        if char == '*':
            starPlacements.append(i)
    return starPlacements

def test_find_stars():
    result = find_stars("467..114..")
    assert len(result) == 0
    result = find_stars("...*......")
    assert len(result) == 1
    assert result[0] == 3

# Open the file in read mode
with open('day3/input_day3.txt', 'r') as file:

    sum = 0
    currentLine = ""
    nextLine = ""
    prevLineNumbers = []
    currentLineNumbers = []
    nextLineNumbers = []

    # Iterate over each line in the file
    for line in file:

        currentLine = nextLine
        nextLine = line.strip()

        prevLineNumbers = currentLineNumbers
        currentLineNumbers = nextLineNumbers
        nextLineNumbers = find_numbers(nextLine)

        stars = find_stars(currentLine)

        for star in stars:
            adjentNumbers = numbers_connecting_star(star, prevLineNumbers, currentLineNumbers, nextLineNumbers)
            if len(adjentNumbers) == 2:
                gear_ratio = int(adjentNumbers[0].group()) * int(adjentNumbers[1].group())
                sum += gear_ratio
    
    print("sum: ", sum)



        
