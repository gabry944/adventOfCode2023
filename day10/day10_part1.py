import pytest

def find_start(lines):   
    loopDict = {}   

    for i, line in enumerate(lines):
        print("line: ", line.strip())
        for j, char in enumerate(line):
            # print("char: ", char)
            if char == 'S':
                loopDict[(i, j)] = 0
                print("pos: ", i, ", ", j)
                print("loopDict: ", loopDict)
                print("loopDict len:", len(loopDict))


    for key, value in loopDict.items():
        print(f"Key: {key}, Value: {value}")

    return loopDict      

def test_find_start():
    with open('day10/test_input.txt', 'r') as file:
        loopDict = find_start(file.readlines())
        assert loopDict == {(1, 1) : 0}

    with open('day10/test_input2.txt', 'r') as file:
        loopDict = find_start(file.readlines())
        assert loopDict == {(2, 0) : 0}


# Main Code
# with open('day10/input.txt', 'r') as file:
#     read_file(file.readlines())