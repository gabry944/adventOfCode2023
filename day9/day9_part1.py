import pytest

def read_file(lines):      

    for i, line in enumerate(lines):
        print("line: ", line.strip())


def test_day9_part1():
    with open('day9/test_input.txt', 'r') as file:
        read_file(file.readlines())
        assert False


# Main Code
with open('day9/input.txt', 'r') as file:
    read_file(file.readlines())