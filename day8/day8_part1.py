import pytest

class NetworkNode:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def print(self):
        print("name: ", self.name, ", left: ", self.left, ", right: ", self.right)

def read_file(lines):      
    instructions = []
    network = []
    for i, line in enumerate(lines):
        line = line.strip()
        if i == 0: # instructions
            for char in line:
                instructions.append(char)
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

            network.append(NetworkNode(name, left, right))
    return instructions, network
  
def test_read_file():
    with open('day8/test_input_day8.txt', 'r') as file:
        instructions, network = read_file(file.readlines())
        assert instructions == ['R', 'L']
        assert network[0].name == "AAA"
        assert network[0].left == "BBB"
        assert network[0].right == "CCC"
        assert network[1].name == "BBB"
        assert network[1].left == "DDD"
        assert network[1].right == "EEE"
        assert network[2].name == "CCC"
        assert network[2].left == "ZZZ"
        assert network[2].right == "GGG"



def test_day8_part1():
    with open('day8/test_input_day8.txt', 'r') as file:
        read_file(file.readlines())
        assert False


# Main Code
with open('day8/input_day8.txt', 'r') as file:
    read_file(file.readlines())