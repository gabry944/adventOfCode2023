import re
import pytest

def find_first_and_last_numbers(input_string):
    # Find all numbers in the string using regular expression
    numbers = re.findall(r'\d+', input_string)

    if numbers:
        # Convert the first and last numbers to sigel digit integers
        first_number_letter = str(numbers)[2]
        first_number = int(first_number_letter)
        last_number = int(numbers[-1]) % 10

        return first_number, last_number
    else:
        # No numbers found in the string
        return None, None
    
def test_find_first_and_last_numbers():
    first, last = find_first_and_last_numbers("1abc2")
    assert first == 1
    assert last == 2
    first, last = find_first_and_last_numbers("pqr3stu8vwx")
    assert first == 3
    assert last == 8

def test_input_day1():
    with open('day1/test_input_day1_part1.txt', 'r') as file:
        sum = 0
        for line in file:
            first, last = find_first_and_last_numbers(line)
            number = first * 10 + last
            sum += number
                 
            print(line.strip())  # strip() removes the newline character at the end of each line
            print("First number:", first, ", Last number:", last, ", number:", number, ", sum:", sum)
            
        assert sum == 142

with open('day1/input_day1.txt', 'r') as file:
    sum = 0
    for line in file:
        first, last = find_first_and_last_numbers(line)
        number = first * 10 + last
        sum = sum + number
    print("sum:", sum)
