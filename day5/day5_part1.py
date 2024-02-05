import pytest
import sys

def read_seeds(input_string):
    seeds = []
    input = input_string.split(':')
    for seed in input[1].strip().split(' '):
        seeds.append(int(seed))
    return seeds

def test_read_seeds():
    input = "seeds: 79 14 55 13"
    assert read_seeds(input) == [79, 14, 55, 13]

def convert_nr(seed, convert_string):     
    destinationStart, sourceStart, rangeLength = map(int, convert_string.split())
    if seed >= sourceStart and seed < sourceStart + rangeLength:
        seed = destinationStart + (seed - sourceStart)
    return seed

def test_convert_nr():
    input = "50 98 2"
    assert convert_nr(97, input) == 97
    assert convert_nr(98, input) == 50
    assert convert_nr(99, input) == 51
    assert convert_nr(100, input) == 100

    input = "52 50 48"
    assert convert_nr(49, input) == 49
    assert convert_nr(50, input) == 52
    assert convert_nr(51, input) == 53
    assert convert_nr(52, input) == 54
    assert convert_nr(96, input) == 98
    assert convert_nr(97, input) == 99
    assert convert_nr(98, input) == 98

def convert_seeds(seeds, convert_strings):
    for i, seed in enumerate(seeds):
        for convert_string in convert_strings:                    
            seed = convert_nr(seed, convert_string)
            if seed != seeds[i]: # test against old value to see if seed has been converted
                print("Seed coverted from ", seeds[i], " to ", seed)
                seeds[i] = seed
                break
    print("Seeds: ", seeds)
    return seeds

def test_convert_seeds():
    seeds = [79, 14, 55, 13]
    convert_strings = ["50 98 2", "52 50 48"]
    seeds = convert_seeds(seeds, convert_strings)
    assert seeds == [81, 14, 57, 13]

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

def test_read_and_convert_seeds():
    with open('day5/test_input_day5.txt', 'r') as file:
        seeds = read_and_convert_seeds(file.readlines())
        assert seeds == [82, 43, 86, 35]

def test_day5_part1():
    with open('day5/test_input_day5.txt', 'r') as file:
        seeds = read_and_convert_seeds(file.readlines())

        lowestLocation = sys.maxsize  
        print('seed: ', seeds)

        for seed in seeds:
            if(seed < lowestLocation):
                lowestLocation = seed
                    
        assert lowestLocation == 35

# Main Code
with open('day5/input_day5.txt', 'r') as file:
    seeds = read_and_convert_seeds(file.readlines())

    lowestLocation = sys.maxsize  
    for seed in seeds:
        if(seed < lowestLocation):
            lowestLocation = seed
                
    print("lowestLocation: ", lowestLocation)