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

def find_start_paths(startPos, lines):

    # test in a cross pattern around the start point (look so that we don't test out of chart)
    # we assume that there is only 2 valid paths from the start point
    startPaths = []
    if startPos[0] - 1 >= 0:    
        up = lines[startPos[0]- 1][startPos[1]]
        if up == "|" or up == "F" or up == "7":
            startPaths.append((startPos[0] - 1, startPos[1]))
    if startPos[0] + 1 < len(lines):
        down = lines[startPos[0] + 1][startPos[1]]
        if down == "|" or down == "L" or down == "J":
            startPaths.append((startPos[0] + 1, startPos[1]))
    if startPos[1] - 1 >= 0:
        left = lines[startPos[0]][startPos[1] - 1]
        if left == "-" or left == "L" or left == "F":
            startPaths.append((startPos[0], startPos[1] - 1))
    if startPos[1] + 1 < len(lines[0]): # all lines have the same length so it's okay to just check against the top line
        right = lines[startPos[0]][startPos[1] + 1]
        if right == "-" or right == "J" or right == "7":
            startPaths.append((startPos[0], startPos[1] + 1))

    return startPaths
        
def test_find_start_paths():
    with open('day10/test_input.txt', 'r') as file:
        lines = file.readlines()
        startPos = (1, 1)

        print("lines:      ", lines)
        print("startPos:   ", startPos)
        print("startRow  = ", lines[startPos[0]].strip())
        print("startPipe = ", lines[startPos[0]][startPos[1]])

        startPaths = find_start_paths(startPos, lines)
        assert len(startPaths) == 2
        assert startPaths == [(2, 1), (1, 2)]

    with open('day10/test_input2.txt', 'r') as file:
        lines = file.readlines()
        startPos = (2, 0)
        startPaths = find_start_paths(startPos, lines)
        assert startPaths == [(3, 0), (2, 1)]
    




# Main Code
# with open('day10/input.txt', 'r') as file:
#     read_file(file.readlines())