import pytest
import sys

def read_file(lines):       

    for i, line in enumerate(lines):
        print("line: ", line.strip())


def test_day6_part1():
    with open('day6/test_input_day6.txt', 'r') as file:
        read_file(file.readlines())
        assert False


# Main Code
with open('day6/input_day6.txt', 'r') as file:
    read_file(file.readlines())