import pytest

def read_file(lines):      

    for i, line in enumerate(lines):
        print("line: ", line.strip())


def test_day8_part1():
    with open('day8/test_input_day8.txt', 'r') as file:
        read_file(file.readlines())
        assert False


# Main Code
with open('day8/input_day8.txt', 'r') as file:
    read_file(file.readlines())