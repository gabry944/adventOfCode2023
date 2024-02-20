import pytest


def continue_loop(position, pipe, direction, loopDict, lines):
    print("position: ", position)
    print("loopDict: ", loopDict)
    print("lines: ", lines)

    # direction is a tuple (row, column) that represents the direction traverse through the pipe -1, 0, 1
    # next position (row, column)

    nextPosition = (0, 0)
    row = 0
    column = 0

    if pipe == "|":
        row = position[0] + direction[0]
        column = position[1]
    
    if pipe == "-":
        row = position[0]
        column = position[1] + direction[1]

    if pipe == "L":
        if direction == (1, 0):
            # row = position[0]
            # column = position[1] + 1
            direction = (0, 1)
        elif direction == (0, -1):
            # row = position[0] - 1 
            # column = position[1]
            direction = (-1, 0)
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False

    if pipe == "J":
        if direction == (1, 0):
            # row = position[0] + 1
            # column = position[1]
            direction = (0, -1)
        elif direction == (0, 1):
            # row = position[0]
            # column = position[1] -1
            direction = (-1, 0)
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False

    if pipe == "7":
        if direction == (1, 0):
            # row = position[0] + 1
            # column = position[1]
            direction = (0, 1)
        elif direction == (0, -1):
            # row = position[0] - 1
            # column = position[1]
            direction = (-1, 0)
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False
    
    if pipe == "F":
        if direction == (0, -1):
            # row = position[0]
            # column = position[1] - 1
            direction = (1, 0)
        elif direction == (-1, 0):
            # row = position[0]
            # column = position[1] + 1
            direction = ( 0, 1)
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False

            
    nextPosition = (position[0] + direction[0], position[1] + direction[1])

    loopDict[nextPosition] = loopDict[position] + 1
    
    return nextPosition, lines[nextPosition[0]][nextPosition[1]], direction, loopDict
    
    
    # if position in loopDict:
    #     print("position already in loopDict")
    #     return loopDict[position], loopDict
    
    # return continue_loop((row, column), lines[row][column], direction, loopDict, lines)

def test_continue_loop():
    with open('day10/test_input.txt', 'r') as file:
        lines = file.readlines()
        position = (2, 1)
        pipe = "|"
        direction = (1, 0)
        loopDict = {(1, 1) : 0, (2, 1) : 1}
        nextPosition, nextPipe, nextDirection, loopDict = continue_loop(position, pipe, direction, loopDict, lines)
        assert nextPosition == (3, 1)
        assert nextPipe == "L"
        assert nextDirection == (1, 0)
        assert loopDict[nextPosition] == 2

        position = nextPosition
        pipe = nextPipe
        direction = nextDirection
        nextPosition, nextPipe, nextDirection, loopDict = continue_loop(position, pipe, direction, loopDict, lines)
        assert nextPosition == (3, 2)
        assert nextPipe == "-"
        assert nextDirection == (0, 1)
        assert loopDict[nextPosition] == 3

        position = nextPosition
        pipe = nextPipe
        direction = nextDirection
        nextPosition, nextPipe, nextDirection, loopDict = continue_loop(position, pipe, direction, loopDict, lines)
        assert nextPosition == (3, 3)
        assert nextPipe == "J"
        assert nextDirection == (0, 1)
        assert loopDict[nextPosition] == 4
      
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