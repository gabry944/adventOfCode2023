import re
import pytest

def spelled_out_to_digit(word):
    # Mapping of spelled-out numbers to digits
    spelled_out_to_digit_mapping = {
        'oneight' : '18',
        'twone' : '21',
        'eightwo': '82',
        'eighthree': '83',
        'fiveight': '58',
        'threeight': '38',
        'nineight': '98',
        'sevenine': '79',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    return spelled_out_to_digit_mapping.get(word.lower(), word)

def find_first_and_last_numbers(input_string):
    # print("input_string", input_string)
    # Find all numbers in the string using regular expression
    numbers = re.findall(r'\d+|oneight|twone|eighthree|eightwo|fiveight|threeight|nineight|sevenine|one|two|three|four|five|six|seven|eight|nine', input_string)
    # print("found numbers", numbers)  

    numbers = [spelled_out_to_digit(number) for number in numbers]
    #p rint("numbers", numbers)

    if numbers:
        # Convert the first and last numbers to singel digit integers
        first_number_letter = str(numbers[0])[0]
        first_number = int(first_number_letter)
        last_number = int(numbers[-1]) % 10

        return first_number, last_number
    else:
        # No numbers found in the string
        return None, None

def test_find_first_and_last_numbers():
    first, last = find_first_and_last_numbers("two1nine")
    assert first == 2
    assert last == 9
    first, last = find_first_and_last_numbers("eightwothree")
    assert first == 8
    assert last == 3

def test_input_day1():
    with open('day1/test_input_day1_part2.txt', 'r') as file:
        sum = 0
        for line in file:
            first, last = find_first_and_last_numbers(line.strip())
            number = first * 10 + last
            sum += number
                    
            print(line.strip())
            numbers = re.findall(r'\d+|twone|eighthree|eightwo|fiveight|threeight|nineight|sevenine|one|two|three|four|five|six|seven|eight|nine', line)
            print("found numbers", numbers)
            numbers = [spelled_out_to_digit(number) for number in numbers]
            print("numbers as digits", numbers)
            print("First number:", first, ", Last number:", last, ", number:", number, ", sum:", sum)

        assert sum == 281

# Open the file in read mode
with open('day1/input_day1.txt', 'r') as file:
    sum = 0
    # Iterate over each line in the file
    for line in file:
        # Process each line as needed
        #first, last = find_first_and_last_numbers(replce_spelled_out_numbers_to_digit(line))
        first, last = find_first_and_last_numbers(line.strip())
        number = first * 10 + last
        sum = sum + number

    print("sum:", sum)
