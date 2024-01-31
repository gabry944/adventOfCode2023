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
    result = winning_numbers("Card   1: 66 92  4 54 39 76 49 27 61 56 | 66 59 85 54 61 86 37 49  6 18 81 39  4 56  2 48 76 72 71 25 27 67 10 92 13")
    assert len(result) == 10
    assert result[0] == 66
    assert result[1] == 92
    assert result[2] == 4
    assert result[3] == 54
    assert result[4] == 39
    assert result[5] == 76
    assert result[6] == 49
    assert result[7] == 27
    assert result[8] == 61
    assert result[9] == 56

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
                copies[nr + i + 1].append(myNumbers)

def test_look_for_matches():
    winning_numbers = [41, 48, 83, 86, 17]
    my_numbers = [83, 86, 6, 31, 17, 9, 48, 53]
    copies = [[] for _ in range(6)]
    look_for_matches(winning_numbers, my_numbers, copies, 0, 6)
    assert len(copies[0]) == 0
    assert len(copies[1]) == 1
    assert copies[1][0] == my_numbers
    assert len(copies[2]) == 1
    assert copies[2][0] == my_numbers
    assert len(copies[3]) == 1
    assert copies[3][0] == my_numbers
    assert len(copies[4]) == 1
    assert copies[4][0] == my_numbers
    assert len(copies[5]) == 0

    winning_numbers = [13, 32, 20, 16, 61]
    my_numbers = [61, 30, 68, 82, 17, 32, 24, 19]    
    look_for_matches(winning_numbers, my_numbers, copies, 1, 6)
    assert len(copies[0]) == 0
    assert len(copies[1]) == 1
    assert len(copies[2]) == 2
    assert copies[2][1] == my_numbers
    assert len(copies[3]) == 2
    assert copies[3][1] == my_numbers
    assert len(copies[4]) == 1
    assert len(copies[5]) == 0


def test_input_day4():
    with open('day4/test_input_day4.txt', 'r') as file:
        sum = 0
        nr = 0

        lines = file.readlines()
        assert len(lines) == 6

        copies = [[] for _ in range(len(lines))]

        for card in lines:

            winningNumbers = winning_numbers(card)
            myNumbers = my_numbers(card)

            print("Card " + str(nr) + ": " + str(winningNumbers) + " | " + str(myNumbers))

            look_for_matches(winningNumbers, myNumbers, copies, nr, len(lines))
            sum += 1
                
            for myCopiedNumbers in copies[nr]:
                look_for_matches(winningNumbers, myNumbers, copies, nr, len(lines))
                sum += 1

            nr += 1

        for i, copy in enumerate(copies):
            print("card ", i , ": ", len(copy) + 1)
        
        print("copies:", copies)

        assert sum == 30

with open('day4/input_day4.txt', 'r') as file:
    sum = 0
    nr = 0

    lines = file.readlines()
    copies = [[] for _ in range(len(lines))]

    for card in lines:

        winningNumbers = winning_numbers(card)
        myNumbers = my_numbers(card)

        look_for_matches(winningNumbers, myNumbers, copies, nr, len(lines))
        sum += 1
            
        for myCopiedNumbers in copies[nr]:
            look_for_matches(winningNumbers, myNumbers, copies, nr, len(lines))
            sum += 1

        nr += 1    
    
    print("sum:", sum)
