import pytest
import sys
import re

def possible_distances(totalTime):
    distances = []
    for holdTime in range(0, totalTime + 1):
        speed = holdTime
        travelTime = totalTime - holdTime
        distances.append(speed * travelTime)

    return distances

def test_possible_distances():
    assert possible_distances(7) == [0, 6, 10, 12, 12, 10, 6, 0]

def read_races(lines):
    times = []
    distances = []

    for line in lines:
        print("line: ", line.strip())
        if "Time:" in line:
            numbers = re.findall(r'\d+', line.strip())
            for number in numbers:
                times.append(int(number))
        if "Distance:" in line:
            numbers = re.findall(r'\d+', line.strip())
            for number in numbers:
                distances.append(int(number))

    return times, distances

def test_read_races():
    with open('day6/test_input_day6.txt', 'r') as file:
        time, distance = read_races(file.readlines())
        assert time == [7, 15, 30]
        assert distance == [9, 40, 200]

def possible_wins(times, records):
        possibleWins = []
        for i, time in enumerate(times):
            possibleDistances = possible_distances(time)
            
            possibleWin = 0
            for possibleDistance in possibleDistances:
                if possibleDistance > records[i]:
                    # print("Possible distance: ", possibleDistance)
                    possibleWin += 1
                    
            possibleWins.append(possibleWin)

        return possibleWins

def test_possible_wins():
    with open('day6/test_input_day6.txt', 'r') as file:
        times, records = read_races(file.readlines())
        possibleWins = possible_wins(times, records)
        assert possibleWins == [4, 8, 9]

def test_day6_part1():
    with open('day6/test_input_day6.txt', 'r') as file:
        times, records = read_races(file.readlines())
        possibleWins = possible_wins(times, records)

        margin = 1
        for wins in possibleWins:
            margin *= wins

        assert margin == 288


# Main Code
with open('day6/input_day6.txt', 'r') as file:
        times, records = read_races(file.readlines())
        possibleWins = possible_wins(times, records)

        margin = 1
        for wins in possibleWins:
            margin *= wins

        print("Result: ", margin) 