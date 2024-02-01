import pytest
import re

def find_numbers(input_string):
    matches = re.finditer(r'\d+', input_string)
    result = [int (match.group()) for match in matches]
    return result

def winning_numbers(input_string):

    WnningPart = input_string.split("|")[0]
    WnningPart = WnningPart.split(":")[1]

    winningNumbers = find_numbers(WnningPart)

    return winningNumbers

def test_winning_numbers():
    result = winning_numbers("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert len(result) == 5
    assert result[0] == 41
    assert result[1] == 48
    assert result[2] == 83
    assert result[3] == 86
    assert result[4] == 17

def my_numbers(input_string):

    myNumbersPart = input_string.split("|")[1]
    myNumbers = find_numbers(myNumbersPart)

    return myNumbers

def test_my_numbers():
    result = my_numbers("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert len(result) == 8
    assert result[0] == 83
    assert result[1] == 86
    assert result[2] == 6
    assert result[3] == 31
    assert result[4] == 17
    assert result[5] == 9
    assert result[6] == 48
    assert result[7] == 53

def matching_numbers(winningNumbers, myNumbers):
    matchingNumbers = 0

    for number in myNumbers:
        if number in winningNumbers:
            matchingNumbers += 1

    return matchingNumbers

def test_matching_numbers():
    winning_numbers = [41, 48, 83, 86, 17]
    my_numbers = [83, 86, 6, 31, 17, 9, 48, 53]
    assert matching_numbers(winning_numbers, my_numbers) == 4
    winning_numbers = [13, 32, 20, 16, 61]
    my_numbers = [61, 30, 68, 82, 17, 32, 24, 19]
    assert matching_numbers(winning_numbers, my_numbers) == 2

def look_for_matches(winningNumbers, myNumbers, copies, nr, lines):
    matches = matching_numbers(winningNumbers, myNumbers)
    if matches > 0:
        for i in range(matches):
            if(nr + i + 1 < lines):
                copies[nr + i + 1] += copies[nr]

def test_look_for_matches():
    winning_numbers = [41, 48, 83, 86, 17]
    my_numbers = [83, 86, 6, 31, 17, 9, 48, 53]
    copies = [1 for _ in range(6)]
    look_for_matches(winning_numbers, my_numbers, copies, 0, 6)
    assert copies[0] == 1
    assert copies[1] == 2
    assert copies[2] == 2
    assert copies[3] == 2
    assert copies[4] == 2
    assert copies[5] == 1

    winning_numbers = [13, 32, 20, 16, 61]
    my_numbers = [61, 30, 68, 82, 17, 32, 24, 19]    
    look_for_matches(winning_numbers, my_numbers, copies, 1, 6)
    assert copies[0] == 1
    assert copies[1] == 2
    assert copies[2] == 4
    assert copies[3] == 4
    assert copies[4] == 2
    assert copies[5] == 1


def test_input_day4():
    with open('day4/test_input_day4.txt', 'r') as file:
        
        lines = file.readlines()
        assert len(lines) == 6
        copies = [1 for _ in range(len(lines))]

        for nr, card in enumerate(lines):
            winningNumbers = winning_numbers(card)
            myNumbers = my_numbers(card)
            print("Card " + str(nr) + ": " + str(winningNumbers) + " | " + str(myNumbers))
            look_for_matches(winningNumbers, myNumbers, copies, nr, len(lines))
            
        sum = 0
        for i, copy in enumerate(copies):
            print("card ", i , ": ", copy)
            sum += copy
        
        assert sum == 30

with open('day4/input_day4.txt', 'r') as file:

    lines = file.readlines()
    copies = [1 for _ in range(len(lines))]

    for nr, card in enumerate(lines):
        winningNumbers = winning_numbers(card)
        myNumbers = my_numbers(card)
        look_for_matches(winningNumbers, myNumbers, copies, nr, len(lines))            
    
    sum = 0
    for i, copy in enumerate(copies):
        sum += copy
    
    print("sum:", sum)
