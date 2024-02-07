import pytest
import math

def read_file(lines):      
    instructions = []
    networkDict = {}
    start = []
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

            # Start on nodes that ends with A
            if name[2] == "A":
                start.append(name)

    return start, instructions, networkDict
  
def test_read_file():
    with open('day8/test_input_day8_part2.txt', 'r') as file:
        start, instructions, network = read_file(file.readlines())
        assert instructions == [0, 1]
        assert network["11A"] == ("11B", "XXX")
        assert network["11B"] == ("XXX", "11Z")
        assert network["11Z"] == ("11B", "XXX")
        assert start == ["11A", "22A"]

def test_day8_part1():
    with open('day8/test_input_day8_part2.txt', 'r') as file:
        positions, instructions, network = read_file(file.readlines())

        stillSearching = True
        steps = 0
        instructions_length = len(instructions)

        while stillSearching:
            stillSearching = False        
            for i, position in enumerate(positions):
                print(f"Step: {steps}, Position: {position}, Instruction: {instructions[steps % instructions_length]}")
                positions[i] = network[position][instructions[steps % instructions_length]]
                if stillSearching == False and positions[i][2] != "Z":
                    stillSearching = True
            steps += 1
        
        assert steps == 6


# Main Code
with open('day8/input_day8.txt', 'r') as file:
    startPositions, instructions, network = read_file(file.readlines())
    print("startPositions: ",len(startPositions), " : ", startPositions)
    
    steps = [0 for i in range(len(startPositions))]
    instructions_length = len(instructions)

    for i, startPosition in enumerate(startPositions):
        position = startPosition
        while position[2] != "Z":
            position = network[position][instructions[steps[i] % instructions_length]]
            steps[i] += 1
    print(f"Steps: {steps}")

    lcm = math.lcm(steps[0], steps[1], steps[2], steps[3], steps[4], steps[5])
    print(f"lcm: {lcm}")