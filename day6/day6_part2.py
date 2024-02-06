import pytest
import re
import cmath
import math

def read_race(lines):
    time = 0
    distance = 0

    for line in lines:
        print("line: ", line.strip())
        if "Time:" in line:
            line = line.replace("Time:", "")
            line = line.replace(" ", "")
            numbers = re.findall(r'\d+', line)
            for number in numbers:
                time = int(number)
        if "Distance:" in line:
            line = line.replace("Distance:", "")
            line = line.replace(" ", "")
            numbers = re.findall(r'\d+', line.strip())
            for number in numbers:
                distance = int(number)

    return time, distance

def test_read_race():
    with open('day6/test_input_day6.txt', 'r') as file:
        time, distance = read_race(file.readlines())
        assert time == 71530
        assert distance == 940200

def possible_wins(time, record):
        possibleWins = 0       

        # Formula for a win is: x * (time - x) > records[i]
        # Can be written as a quadratic equation: -1 * x^2 + x * time - records[i] > 0  

        # Solve the quadratic equation ax**2 + bx + c = 0
        a = -1
        b = time
        c = -(record + 1) # +1 to make sure the equation is greater than 0

        # calculate the discriminant
        d = (b**2) - (4*a*c)

        # find two solutions
        sol1 = (-b-cmath.sqrt(d))/(2*a)
        sol2 = (-b+cmath.sqrt(d))/(2*a)

        print("time: ", time, " record: ", record)
        print("sol1: ", sol1, " sol2: ", sol2)

        sol1 = math.floor(sol1.real)
        sol2 = math.ceil(sol2.real)

        print("sol1: ", sol1, " sol2: ", sol2)
        possibleWins = sol1 - sol2 + 1 # +1 to include the sol2 value
        print("possibleWins: ", possibleWins)
                    
        return possibleWins

def test_possible_wins():
    with open('day6/test_input_day6.txt', 'r') as file:
        time, record = read_race(file.readlines())
        possibleWins = possible_wins(time, record)
        assert possibleWins == 71503


# Main Code
with open('day6/input_day6.txt', 'r') as file:
        time, record = read_race(file.readlines())
        possibleWins = possible_wins(time, record)

        print("Result: ", possibleWins) 