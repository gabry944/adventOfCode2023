import pytest

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

        steps = 0
        stillSearching = True

        while stillSearching:

            stillSearching = False
            
            for i, position in enumerate(positions):
                left, right = network[position]
                print(f"Current: {position}, Left: {left}, Right: {right}")
                if instructions[steps % len(instructions)] == 1:
                    positions[i] = right
                else:
                    positions[i] = left

                if positions[i][2] != "Z":
                    stillSearching = True
            steps += 1
        
        assert steps == 6


# Main Code
# with open('day8/input_day8.txt', 'r') as file:
#     positions, instructions, network = read_file(file.readlines())

#     steps = 0
#     stillSearching = True

#     while stillSearching:

#         stillSearching = False
        
#         for i, position in enumerate(positions):
#             left, right = network[position]
#             if instructions[steps % len(instructions)] == 1:
#                 positions[i] = right
#             else:
#                 positions[i] = left

#             if positions[i][2] != "Z":
#                 stillSearching = True
#         steps += 1        
    
#     print(f"Steps: {steps}")