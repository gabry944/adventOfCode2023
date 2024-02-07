import pytest

def read_file(lines):      
    instructions = []
    networkDict = {}
    for i, line in enumerate(lines):
        line = line.strip()
        if i == 0: # instructions
            for char in line:
                if char == "R":
                    instructions.append(1)
                elif char == "L":
                    instructions.append(0)
        if i > 1: # nodes
            name = ""
            left = ""
            right = ""

            parts = line.split("=")
            name = parts[0].strip()

            parts = parts[1].strip().replace("(", "").replace(")", "")
            parts = parts.split(", ")
            left = parts[0]
            right = parts[1]
            networkDict[name] = (left, right)
    return instructions, networkDict
  
def test_read_file():
    with open('day8/test_input_day8.txt', 'r') as file:
        instructions, network = read_file(file.readlines())
        assert instructions == [0, 0, 1]
        assert network["AAA"] == ("BBB", "BBB")
        assert network["BBB"] == ("AAA", "ZZZ")
        assert network["ZZZ"] == ("ZZZ", "ZZZ")


def test_day8_part1():
    with open('day8/test_input_day8.txt', 'r') as file:
        instructions, network = read_file(file.readlines())

        steps = 0
        current = "AAA"

        while current != "ZZZ":
            left, right = network[current]
            print(f"Current: {current}, Left: {left}, Right: {right}")
            if instructions[steps % len(instructions)] == 1:
                current = right
            else:
                current = left
            steps += 1
        
        assert steps == 6


# Main Code
with open('day8/input_day8.txt', 'r') as file:
    instructions, network = read_file(file.readlines())

    steps = 0
    current = "AAA"

    while current != "ZZZ":
        left, right = network[current]
        if instructions[steps % len(instructions)] == 1:
            current = right
        else:
            current = left
        steps += 1
    
    print(f"Steps: {steps}")