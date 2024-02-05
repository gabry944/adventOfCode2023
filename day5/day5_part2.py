import pytest
import sys

def read_seeds(input_string):
    seeds = []
    input = input_string.split(':')
    start = 0
    for nr in input[1].strip().split(' '):
        if start == 0:
            start = int(nr)
        else:
            seeds.append((start, int(nr)))
            start = 0
    return seeds

def test_read_seeds():
    input = "seeds: 79 14 55 13"
    output = read_seeds(input)
    assert output == [(79, 14), (55, 13)]
    assert output[0] == (79, 14)
    assert output[1] == (55, 13)
    assert output[0][0] == 79
    assert output[0][1] == 14
    assert output[1][0] == 55
    assert output[1][1] == 13

def convert_nr(seeds, index, convert_string):
    seedStart, seedLenght = seeds[index]
    destinationStart, sourceStart, rangeLength = map(int, convert_string.split())

    # If seed ranges start before the conversions source range and first part of the seed will not convert
    if seedStart < sourceStart and seedStart + seedLenght > sourceStart:
        firstPartSeedLenght = sourceStart - seedStart
        seeds.append((seedStart, firstPartSeedLenght))

        # Remaining seed that should be converted
        seedStart = sourceStart
        seedLenght = seedLenght - firstPartSeedLenght

    if seedStart >= sourceStart and seedStart < sourceStart + rangeLength:

        # If seed ranges end after the conversions source range and last part of the seed will not convert
        if seedStart + seedLenght > sourceStart + rangeLength:
            lastPartSeedLenght = (seedStart + seedLenght) - (sourceStart + rangeLength)
            seeds.append((sourceStart + rangeLength, lastPartSeedLenght))
            seedLenght = seedLenght - lastPartSeedLenght

        # conversion
        seedStart = destinationStart + (seedStart - sourceStart)
        seeds[index] = (seedStart, seedLenght)

    return seeds

def test_convert_nr():
    seeds = [(79, 14), (55, 13)]
    assert len(seeds) == 2

    input = "50 98 2"
    for i, seed in enumerate(seeds):
        seeds = convert_nr(seeds, i, input)
    assert len(seeds) == 2
    assert seeds == [(79, 14), (55, 13)]

    input = "52 50 48"
    for i in range(len(seeds)):
        seeds = convert_nr(seeds, i, input)
    assert len(seeds) == 2
    assert seeds == [(81, 14), (57, 13)]

    # Test where seed range exceeds the conversion range
    input = "20 80 4"
    for i in range(len(seeds)):
        print("Seed nr ", i, " : ", seeds[i])
        seeds = convert_nr(seeds, i, input)
    assert len(seeds) == 3
    assert seeds == [(21, 3), (57, 13), (84, 11)]

    print(" ---- ")

    # Test where seed range starts before conversion range
    input = "200 90 20"
    for i, seed in enumerate(seeds):
        print("Seed nr ", i, " : ", seeds[i])
        seeds = convert_nr(seeds, i, input)
    assert len(seeds) == 4
    assert seeds[0] == (21, 3)
    assert seeds[1] == (57, 13)
    assert seeds[2] == (200, 5)
    assert seeds[3] == (84, 6)
    assert seeds == [(21, 3), (57, 13), (200, 5), (84, 6)]


def convert_seeds(seeds, convert_strings):    
    for i, seed in enumerate(seeds):
        for convert_string in convert_strings:                    
            seeds = convert_nr(seeds, i, convert_string)
            if seed != seeds[i]: # test against old value to see if seed has been converted
                break
        # print("Seed nr ", i, " : ", seed, "convert to: ", seeds[i], " -- seeds: ", seeds)
            
    return seeds

def test_convert_seeds():
    seeds = [(79, 14), (55, 13)]
    convert_strings = ["50 98 2", "52 50 48"]
    seeds = convert_seeds(seeds, convert_strings)
    assert seeds == [(81, 14), (57, 13)]

def read_and_convert_seeds(lines):
    seeds = []
    converters = []         

    for i, line in enumerate(lines):
        if i == 0:
            seeds = read_seeds(line.strip())
        elif len(line.split(':')) == 2:
            continue
        elif line == "\n":
            convert_seeds(seeds, converters)          
            converters = []
        else:            
            converters.append(line.strip())
    convert_seeds(seeds, converters)

    return seeds


def test_day5_part1():
    with open('day5/test_input_day5.txt', 'r') as file:
        seeds = read_and_convert_seeds(file.readlines())

        lowestLocation = sys.maxsize  
        print('seed: ', seeds)

        for seed in seeds:
            if(seed[0] < lowestLocation):
                lowestLocation = seed[0]

        print("lowestLocation: ", lowestLocation) 
        assert lowestLocation == 46

# Main Code
with open('day5/input_day5.txt', 'r') as file:
    seeds = read_and_convert_seeds(file.readlines())

    lowestLocation = sys.maxsize  
    for seed in seeds:
        if(seed[0] < lowestLocation):
            lowestLocation = seed[0]
                
    print("lowestLocation: ", lowestLocation)