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
        insideDirection = "right"
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

        position = nextPosition
        direction = nextDirection
        nextPosition, nextDirection= continue_loop(position, direction, lines)
        assert nextPosition == (2, 3)
        assert lines[nextPosition[0]][nextPosition[1]] == "|"
        assert nextDirection == (-1, 0)


def get_inside(pipe, direction, insideDirection):
    # direction is a tuple (row, column) that represents the direction traverse through the pipe -1, 0, 1
    # pipe is a string that represents the current pipe at the position
    # insideDirection is a string that represents the direction that faces inside the loop
    
    insideDirections = []
    nextInsideDirection = insideDirection

    if pipe == "|" or pipe == "-":
        insideDirections.append(insideDirection)

    if pipe == "L":
        if direction == (1, 0):
            if insideDirection == "right":
                nextInsideDirection = "up"
            elif insideDirection == "left":
                insideDirections.append("left")
                insideDirections.append("down")
                nextInsideDirection = "down"
        elif direction == (0, -1):
            if insideDirection == "up":
                nextInsideDirection = "right"
            elif insideDirection == "down":
                insideDirections.append("down")
                insideDirections.append("left")
                nextInsideDirection = "left"
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False
    elif pipe == "J":
        if direction == (1, 0):
            if insideDirection == "right":
                insideDirections.append("right")
                insideDirections.append("down")
                nextInsideDirection = "down"
            elif insideDirection == "left":
                nextInsideDirection = "up"
        elif direction == (0, 1):
            if insideDirection == "up":
                nextInsideDirection = "left"
            elif insideDirection == "down":
                insideDirections.append("down")
                insideDirections.append("right")
                nextInsideDirection = "right"
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False
    elif pipe == "7":
        if direction == (-1, 0):
            if insideDirection == "left":
                nextInsideDirection = "down"
            elif insideDirection == "right":
                insideDirections.append("right")
                insideDirections.append("up")
                nextInsideDirection = "up"
        elif direction == (0, 1):
            if insideDirection == "down":
                nextInsideDirection = "left"
            elif insideDirection == "up":
                insideDirections.append("up")
                insideDirections.append("right")
                nextInsideDirection = "right"
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False    
    elif pipe == "F":
        if direction == (0, -1):
            if insideDirection == "down":
                nextInsideDirection = "right"
            elif insideDirection == "up":
                insideDirections.append("up")
                insideDirections.append("left")
                nextInsideDirection = "left"
        elif direction == (-1, 0):
            if insideDirection == "right":
                nextInsideDirection = "down"
            elif insideDirection == "left":
                insideDirections.append("left")
                insideDirections.append("up")
                nextInsideDirection = "up"
        else:
            print("Error: direction: ", direction, " at pipe: ", pipe)
            return False

    # Next position (row, column)     
    return insideDirections, nextInsideDirection

def test_get_inside():
    with open('day10/test_input.txt', 'r') as file:
        lines = file.readlines()
        position = (2, 1)
        direction = (1, 0)
        insideDirection = "right"
        pipe = lines[position[0]][position[1]]
        insideDirections, nextInsideDirection = get_inside(pipe, direction, insideDirection)
        assert insideDirections == ["right"]
        assert nextInsideDirection == "right"

        insideDirection = nextInsideDirection      
        position, direction = continue_loop(position, direction, lines)
        pipe = lines[position[0]][position[1]]
        insideDirections, nextInsideDirection = get_inside(pipe, direction, insideDirection)
        assert insideDirections == []
        assert nextInsideDirection == "up"

        insideDirection = nextInsideDirection      
        position, direction = continue_loop(position, direction, lines)
        pipe = lines[position[0]][position[1]]
        insideDirections, nextInsideDirection = get_inside(pipe, direction, insideDirection)
        assert insideDirections == ["up"]
        assert nextInsideDirection == "up"

        insideDirection = nextInsideDirection      
        position, direction = continue_loop(position, direction, lines)
        pipe = lines[position[0]][position[1]]
        insideDirections, nextInsideDirection = get_inside(pipe, direction, insideDirection)
        assert insideDirections == []
        assert nextInsideDirection == "left"
      
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

def get_start_pipe_and_possible_inside_directions(direction1, direction2):
    # OBS this is a guess that are based on the turn of the start position but it might be the other way around
    if direction1 == (1, 0):
        if direction2 == (-1, 0):
            return "-", "down", "down"
        elif direction2 == (0, 1):
            return "F", "right", "down"
        elif direction2 == (0, -1):
            return "7", "left", "down"
    elif direction1 == (-1, 0):
        if direction2 == (1, 0):
            return "-", "up", "up"
        elif direction2 == (0, 1):
            return "L", "right", "up"
        elif direction2 == (0, -1):
            return "J", "left", "up"
    elif direction1 == (0, 1):
        if direction2 == (0, -1):
            return "|", "left", "left"
        elif direction2 == (1, 0):
            return "F", "down", "left"
        elif direction2 == (-1, 0):
            return "7", "up", "left"
    elif direction1 == (0, -1):
        if direction2 == (0, 1):
            return "|", "right", "right"
        elif direction2 == (1, 0):
            return "L" , "down", "right"
        elif direction2 == (-1, 0):
            return "J", "up", "right"
        
    
def get_loop(startPaths, startPos, lines):
    position1 = startPaths[0]
    direction1 = (position1[0] - startPos[0], position1[1] - startPos[1])
    position2 = startPaths[1]
    direction2 = (position2[0] - startPos[0], position2[1] - startPos[1])

    startPipe, insideDirection1, insideDirection2 = get_start_pipe_and_possible_inside_directions(direction1, direction2)

    # loopDict is a dictionary of the loop, with the position as key and the pipe as value
    loopDict = {startPos : startPipe, startPaths[0] : lines[startPaths[0][0]][startPaths[0][1]], startPaths[1] : lines[startPaths[1][0]][startPaths[1][1]]}

    while True:
        nextPosition1, direction1= continue_loop(position1, direction1, lines)
        if nextPosition1 in loopDict:
            # if position1 is already in loopDict we have closed the loop and can return the loopDict
            return loopDict
        else:
            # As we know the next position already, add it to the loopDict for the next iteration
            loopDict[nextPosition1] = lines[nextPosition1[0]][nextPosition1[1]] 
            position1 = nextPosition1

        nextPosition2, direction2= continue_loop(position2, direction2, lines)
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


def add_tiles(position, insideDirections, loopDict, enclosedTilesDict, lines):
    outsideOfLoop = False
    for inside in insideDirections:
        noWall = True
        step = 1
        tile = position
        while noWall:
            if inside == "up":
                tile = (position[0] - step, position[1])
            elif inside == "down":
                tile = (position[0] + step, position[1])
            elif inside == "left":
                tile = (position[0], position[1] - step)
            elif inside == "right":
                tile = (position[0], position[1] + step)

            if  tile[0] >= len(lines) or tile[1] >= len(lines[0]) or tile[0] < 0 or tile[1] < 0:
                print("We are outside the map (", tile, ")")
                OutsideOfLoop = True
                return OutsideOfLoop, enclosedTilesDict

            if tile in loopDict:
                noWall = False
            else:
                enclosedTilesDict[tile] = 1
                step += 1
    return outsideOfLoop, enclosedTilesDict

def follow_inside_of_loop(startPosition, direction, lines, insideDirection, loopDict):
    position = startPosition
    outsideOfLoop = False
    enclosedTilesDict = {}

    while True:
        pipe = loopDict[position]
        insideDirections, nextInsideDirection = get_inside(pipe, direction, insideDirection)
        outsideOfLoop, enclosedTilesDict = add_tiles(position, insideDirections, loopDict, enclosedTilesDict, lines)
        if outsideOfLoop:
            return outsideOfLoop, len(enclosedTilesDict)

        nextPosition, direction = continue_loop(position, direction, lines)
        position = nextPosition
        insideDirection = nextInsideDirection

        nextPipe = lines[position[0]][position[1]]
        if nextPipe == "S":
            # We are back at the start position, check corresponding tiles and then return the result
            pipe = loopDict[position] # convert the S to the corresponding pipe, that we added to the loopDict before
            insideDirections, nextInsideDirection = get_inside(pipe, direction, insideDirection)
            outsideOfLoop, enclosedTilesDict = add_tiles(position, insideDirections, loopDict, enclosedTilesDict, lines)
            return outsideOfLoop, len(enclosedTilesDict)
        
def reverse_inside_direction(insideDirection):
    if  insideDirection == "up":
        return"down"
    elif insideDirection == "down":
        return "up"
    elif insideDirection == "left":
        return "right"
    elif insideDirection == "right":
        return"left"

def count_enclosed_tiles(startPaths, startPos, lines, loopDict):
    position = startPaths[0]
    direction = (position[0] - startPos[0], position[1] - startPos[1])
    position2 = startPaths[1]
    direction2 = (position2[0] - startPos[0], position2[1] - startPos[1])
    startPipe, insideDirection, insideDirection2 = get_start_pipe_and_possible_inside_directions(direction, direction2)

    OutsideOfLoop, numberEnclosedTiles = follow_inside_of_loop(startPaths[0], direction, lines, insideDirection, loopDict)

    #retry with inverted assumption about that is inside and outside the loop
    if OutsideOfLoop:
        OutsideOfLoop, numberEnclosedTiles = follow_inside_of_loop(startPaths[0], direction, lines, reverse_inside_direction(insideDirection), loopDict)
        
    if OutsideOfLoop:
        print("Something went wrong, we are outside the map again")
        return False
    else:
        return numberEnclosedTiles
        
def test_count_enclosed_tiles():
    with open('day10/test_input.txt', 'r') as file:
        lines = file.readlines()
        startPos = find_start(lines)
        print("startPos: ", startPos)
        startPaths = find_start_paths(startPos, lines)
        print("startPaths: ", startPaths)
        loopDict = get_loop(startPaths, startPos, lines)
        print("loopDict: ", loopDict)
        numberEnclosedTiles = count_enclosed_tiles(startPaths, startPos, lines, loopDict)
        assert numberEnclosedTiles == 1

    with open('day10/test_input2.txt', 'r') as file:
        lines = file.readlines()
        startPos = find_start(lines)
        startPaths = find_start_paths(startPos, lines)
        loopDict = get_loop(startPaths, startPos, lines)
        numberEnclosedTiles = count_enclosed_tiles(startPaths, startPos, lines, loopDict)
        assert numberEnclosedTiles == 1

    with open('day10/test_input3.txt', 'r') as file:
        lines = file.readlines()
        startPos = find_start(lines)
        startPaths = find_start_paths(startPos, lines)
        loopDict = get_loop(startPaths, startPos, lines)
        numberEnclosedTiles = count_enclosed_tiles(startPaths, startPos, lines, loopDict)
        assert numberEnclosedTiles == 4
        
    with open('day10/test_input4.txt', 'r') as file:
        lines = file.readlines()
        startPos = find_start(lines)
        startPaths = find_start_paths(startPos, lines)
        loopDict = get_loop(startPaths, startPos, lines)
        numberEnclosedTiles = count_enclosed_tiles(startPaths, startPos, lines, loopDict)
        assert numberEnclosedTiles == 4

    with open('day10/test_input5.txt', 'r') as file:
        lines = file.readlines()
        startPos = find_start(lines)
        startPaths = find_start_paths(startPos, lines)
        loopDict = get_loop(startPaths, startPos, lines)
        numberEnclosedTiles = count_enclosed_tiles(startPaths, startPos, lines, loopDict)
        assert numberEnclosedTiles == 8

    with open('day10/test_input6.txt', 'r') as file:
        lines = file.readlines()
        startPos = find_start(lines)
        startPaths = find_start_paths(startPos, lines)
        loopDict = get_loop(startPaths, startPos, lines)
        numberEnclosedTiles = count_enclosed_tiles(startPaths, startPos, lines, loopDict)
        assert numberEnclosedTiles == 10


# Main Code
with open('day10/input.txt', 'r') as file:
    lines = file.readlines()
    startPos = find_start(lines)
    startPaths = find_start_paths(startPos, lines)
    loopDict = get_loop(startPaths, startPos, lines)
    numberEnclosedTiles = count_enclosed_tiles(startPaths, startPos, lines, loopDict)
    print("Number enclosed tiles by the loop: ", numberEnclosedTiles)