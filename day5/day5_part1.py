import pytest
import sys

def add_to_convertion_table(input_string, source, destination):
    destinationStart, sourceStart, rangeLength = map(int, input_string.split())
    for i in range(rangeLength):
        source.append(sourceStart + i)
        destination.append(destinationStart + i)

def test_add_to_convertion_table():
    source = []
    destination = []

    input = "50 98 2"
    add_to_convertion_table(input, source, destination)
    assert source == [98, 99]
    assert destination == [50, 51]
    
    input = "52 50 48"
    add_to_convertion_table(input, source, destination)
    assert source ==        [98, 99, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]
    assert destination ==   [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

   
def read_seeds(input_string):
    seeds = []
    input = input_string.split(':')
    for seed in input[1].strip().split(' '):
        seeds.append(int(seed))
    return seeds

def test_read_seeds():
    input = "seeds: 79 14 55 13"
    assert read_seeds(input) == [79, 14, 55, 13]


def read_ranges(lines):
    seeds = []
    converters = []
    source = []
    destination = []           

    for i, line in enumerate(lines):
        if i == 0:
            seeds = read_seeds(line.strip())
        elif len(line.split(':')) == 2:
            continue
        elif line == "\n":
            converters.append((source, destination))
            source = []
            destination = []
        else:
            add_to_convertion_table(line.strip(), source, destination)
    converters.append((source, destination))

    return seeds, converters

def test_read_ranges():
    with open('day5/test_input_day5.txt', 'r') as file:

        seeds, converters = read_ranges(file.readlines())
        # seeds = []
        # converters = []
        # source = []
        # destination = []           

        # lines = file.readlines()
        # for i, line in enumerate(lines):
        #     if i == 0:
        #         seeds = read_seeds(line.strip())
        #     elif len(line.split(':')) == 2:
        #         continue
        #     elif line == "\n":
        #         converters.append((source, destination))
        #         source = []
        #         destination = []
        #     else:
        #         add_to_convertion_table(line.strip(), source, destination)
        # converters.append((source, destination))

        print(converters)
        assert seeds == [79, 14, 55, 13]
        assert converters[0] == ([], [])
        assert converters[1][0] == [98, 99, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]
        assert converters[1][1] == [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


def test_seed_to_map():
    with open('day5/test_input_day5.txt', 'r') as file:
        seeds, converters = read_ranges(file.readlines())

        lowestLocation = sys.maxsize  
        location = []
        print(seeds)
        print(converters)

        for seed in seeds:
            for converter in converters:
                if seed in converter[0]:
                    index = converter[0].index(seed)
                    seed = converter[1][index]
                    print("Seed coverted from ",converter[0][index], " to ", seed)
            location.append(seed)
            if(seed < lowestLocation):
                lowestLocation = seed
                    
        print(location)

        assert location[0] == 82
        assert location[1] == 43
        assert location[2] == 86
        assert location[3] == 35

# Main Code
with open('day5/input_day5.txt', 'r') as file:
    seeds, converters = read_ranges(file.readlines())

    lowestLocation = sys.maxsize  
    location = []
    print("seeds: ", seeds)

    for seed in seeds:
        for converter in converters:
            if seed in converter[0]:
                index = converter[0].index(seed)
                seed = converter[1][index]
        location.append(seed)
        if(seed < lowestLocation):
            lowestLocation = seed
                
    print("lowestLocation: ", lowestLocation)