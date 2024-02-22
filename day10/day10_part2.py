import pytest

def continue_loop(position, direction, lines):
    # direction is a tuple (row, column) that represents the direction traverse through the pipe -1, 0, 1
    # position is a tuple (row, column) that represents the current position in the loop
    # lines is a list of strings that represents the map of the area
    # pipe is a string that represents the current pipe at the position
    pipe = lines[position[0]][position[1]]
    
    if pipe == "L":
        if direction == (1, 0):
            direction = (0, 1)
        elif direction == (0, -1):
            direction = (-1, 0)
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False
    elif pipe == "J":
        if direction == (1, 0):
            direction = (0, -1)
        elif direction == (0, 1):
            direction = (-1, 0)
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False
    elif pipe == "7":
        if direction == (-1, 0):
            direction = (0, -1)
        elif direction == (0, 1):
            direction = (1, 0)
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False    
    elif pipe == "F":
        if direction == (0, -1):
            direction = (1, 0)
        elif direction == (-1, 0):
            direction = (0, 1)
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False

    # Next position (row, column)     
    nextPosition = (position[0] + direction[0], position[1] + direction[1])
    return nextPosition, direction

def test_continue_loop():
    with open('day10/test_input.txt', 'r') as file:
        lines = file.readlines()
        position = (2, 1)
        direction = (1, 0)
        nextPosition, nextDirection = continue_loop(position, direction, lines)
        assert nextPosition == (3, 1)
        assert lines[nextPosition[0]][nextPosition[1]] == "L"
        assert nextDirection == (1, 0)

        position = nextPosition
        direction = nextDirection
        nextPosition, nextDirection = continue_loop(position, direction, lines)
        assert nextPosition == (3, 2)
        assert lines[nextPosition[0]][nextPosition[1]] == "-"
        assert nextDirection == (0, 1)

        position = nextPosition
        direction = nextDirection
        nextPosition, nextDirection = continue_loop(position, direction, lines)
        assert nextPosition == (3, 3)
        assert lines[nextPosition[0]][nextPosition[1]] == "J"
        assert nextDirection == (0, 1)
      
def find_start(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'S':
                return (i, j)
    print("Error: No start position found")
    return False

def test_find_start():
    with open('day10/test_input.txt', 'r') as file:
        startPos = find_start(file.readlines())
        assert startPos == (1, 1)

    with open('day10/test_input2.txt', 'r') as file:
        startPos = find_start(file.readlines())
        assert startPos == (2, 0)

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

def get_start_pipe(direction1, direction2):
    if direction1 == (1, 0):
        if direction2 == (-1, 0):
            return "-"
        elif direction2 == (0, 1):
            return "F"
        elif direction2 == (0, -1):
            return "L"
    elif direction1 == (-1, 0):
        if direction2 == (1, 0):
            return "-"
        elif direction2 == (0, 1):
            return "7"
        elif direction2 == (0, -1):
            return "J"
    elif direction1 == (0, 1):
        if direction2 == (0, -1):
            return "|"
        elif direction2 == (1, 0):
            return "F"
        elif direction2 == (-1, 0):
            return "7"
    elif direction1 == (0, -1):
        if direction2 == (0, 1):
            return "|"
        elif direction2 == (1, 0):
            return "L"
        elif direction2 == (-1, 0):
            return "J"

    
def get_loop(startPaths, startPos, lines):
    position1 = startPaths[0]
    direction1 = (position1[0] - startPos[0], position1[1] - startPos[1])
    position2 = startPaths[1]
    direction2 = (position2[0] - startPos[0], position2[1] - startPos[1])

    # loopDict is a dictionary of the loop, with the position as key and the pipe as value
    loopDict = {startPos : get_start_pipe(direction1, direction2), startPaths[0] : lines[startPaths[0][0]][startPaths[0][1]], startPaths[1] : lines[startPaths[1][0]][startPaths[1][1]]}

    while True:
        nextPosition1, direction1 = continue_loop(position1, direction1, lines)
        if nextPosition1 in loopDict:
            # if position1 is already in loopDict we have closed the loop and can return the loopDict
            return loopDict
        else:
            # As we know the next position already, add it to the loopDict for the next iteration
            loopDict[nextPosition1] = lines[nextPosition1[0]][nextPosition1[1]]
            position1 = nextPosition1

        nextPosition2, direction2 = continue_loop(position2, direction2, lines)
        if nextPosition2 in loopDict:
            return loopDict
        else:
            loopDict[nextPosition2] = lines[nextPosition2[0]][nextPosition2[1]]
            position2 = nextPosition2
            
def test_get_loop():
    with open('day10/test_input.txt', 'r') as file:
        lines = file.readlines()
        print("lines: ", lines)
        startPos = find_start(lines)
        print("startPos: ", startPos)
        assert startPos == (1, 1)
        startPaths = find_start_paths(startPos, lines)
        print("startPaths: ", startPaths)
        assert len(startPaths) == 2
        assert startPaths == [(2, 1), (1, 2)]

        loopDict = get_loop(startPaths, startPos, lines)
        print("loopDict: ", loopDict)
        assert loopDict == {(1, 1): 'F', (2, 1): '|', (1, 2): '-', (3, 1): 'L', (1, 3): '7', (3, 2): '-', (2, 3): '|', (3, 3): 'J'}

    with open('day10/test_input2.txt', 'r') as file:
        lines = file.readlines()
        startPos = find_start(lines)
        startPaths = find_start_paths(startPos, lines)
        loopDict = get_loop(startPaths, startPos, lines)
        print("loopDict: ", loopDict)
        assert loopDict == {(2, 0): 'F', (3, 0): '|', (2, 1): 'J', (4, 0): 'L', (1, 1): 'F', (4, 1): 'J', (1, 2): 'J', (3, 1): 'F', (0, 2): 'F', (3, 2): '-', (0, 3): '7', (3, 3): '-', (1, 3): '|', (3, 4): 'J', (2, 3): 'L', (2, 4): '7'}

# Main Code
with open('day10/input.txt', 'r') as file:
    lines = file.readlines()
    startPos = find_start(lines)
    startPaths = find_start_paths(startPos, lines)
    outline = get_loop(startPaths, startPos, lines)
    # numberEnclosedTiles = count_enclosed_tiles(outline, lines)
    # print("Number enclosed tiles by the loop: ", numberEnclosedTiles)