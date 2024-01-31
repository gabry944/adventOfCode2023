import pytest
import re

def find_numbers(input_string):
    # Use regular expression to find all numbers
    matches = re.finditer(r'\d+', input_string)
    # Collect positions and numbers
    result = [int (match.group()) for match in matches]
    return result


def winning_numbers(input_string):

    WnningPart = input_string.split("|")[0]
    WnningPart = WnningPart.split(":")[1]

    winningNumbers = find_numbers(WnningPart)

    # result.append(int(input_string[10:12]))
    # result.append(int(input_string[13:15]))
    # result.append(int(input_string[16:18]))
    # result.append(int(input_string[19:21]))
    # result.append(int(input_string[22:24]))
    # result.append(int(input_string[25:27]))
    # result.append(int(input_string[28:30]))
    # result.append(int(input_string[31:33]))
    # result.append(int(input_string[34:36]))
    # result.append(int(input_string[37:39]))

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

def card_points(input_string):

    cardPoints = 0
    matchingNumbers = 0
    winningNumbers = winning_numbers(input_string)
    myNumbers = my_numbers(input_string)

    for number in myNumbers:
        if number in winningNumbers:
            matchingNumbers += 1

    if matchingNumbers > 0:
        cardPoints = pow(2, matchingNumbers - 1)

    return cardPoints

def test_card_points():
    assert card_points("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == 8
    assert card_points("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19") == 2
    assert card_points("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1") == 2
    assert card_points("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83") == 1
    assert card_points("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36") == 0
    assert card_points("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11") == 0

def test_input_day4():
    with open('day4/test_input_day4.txt', 'r') as file:
        sum = 0
        for line in file:
            sum += card_points(line)
        assert sum == 13

with open('day4/input_day4.txt', 'r') as file:
    sum = 0
    for line in file:
        sum += card_points(line)
    print("sum: ", sum)