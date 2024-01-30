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

# Open the file in read mode
with open('day3/test_input_day3.txt', 'r') as file:

    sum = 0
    lineNr = 0
    prevLine = ""
    currentLine = ""
    nextLine = ""
    prevLineSpecialCharIndices = []
    currentLineSpecialCharIndices = []
    nextLineSpecialCharIndices = []

    # Iterate over each line in the file
    for line in file:

        prevLine = currentLine
        currentLine = nextLine
        nextLine = line.strip()
        print(currentLine)  # strip() removes the newline character at the end of each line

        prevLineSpecialCharIndices = currentLineSpecialCharIndices
        currentLineSpecialCharIndices = nextLineSpecialCharIndices
        nextLineSpecialCharIndices = find_special_char_indices(nextLine.strip())
        print("special_char_indices: ", prevLineSpecialCharIndices)
        print("special_char_indices: ", currentLineSpecialCharIndices)
        print("special_char_indices: ", nextLineSpecialCharIndices)

        numbers = find_numbers(currentLine)
        print("numbers: ", numbers)

        for number in numbers:
            add = False
            print("number: ", number, ", start: ", number.start(), ", end: ", number.end(), ", group: ", number.group())
            
            for specialCharPos in prevLineSpecialCharIndices:
                #print("prevSpecialCharPos: ", specialCharPos)
                if specialCharPos >= max(number.start() - 1, 0) and specialCharPos <= number.end():
                    add = True
            for specialCharPos in currentLineSpecialCharIndices:
                # print("currentSpecialCharPos: ", specialCharPos)
                # print("max(number.start() - 1, 0) : ", max(number.start() - 1, 0))
                # print("number.end(): ", number.end())
                if specialCharPos >= max(number.start() - 1, 0) and specialCharPos <= number.end():
                    add = True
            for specialCharPos in nextLineSpecialCharIndices:
                #print("nextSpecialCharPos: ", specialCharPos)
                #print("max(number.start() - 1, 0) : ", max(number.start() - 1, 0))
                #print("number.end(): ", number.end())
                if specialCharPos >= max(number.start() - 1, 0) and specialCharPos <= number.end():
                    add = True

            if add == True:
                print("add: ", int(number.group()))
                sum += int(number.group())

        lineNr += 1
    
    print("sum: ", sum)



        
