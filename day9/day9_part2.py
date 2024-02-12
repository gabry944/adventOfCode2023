import pytest


def sequence_of_differences(input):
    differences = []
    allZeros = True
    for i in range(1, len(input)):
        differences.append(input[i] - input[i-1])
        if differences[i-1] != 0:
            allZeros = False
    return differences, allZeros
    
def test_sequence_of_differences():
    assert sequence_of_differences([0, 3, 6, 9, 12, 15]) == ([3, 3, 3, 3, 3], False)
    assert sequence_of_differences([3, 3, 3, 3, 3]) == ([0, 0, 0, 0], True)

def predict_prev(history):    
    prev = 0
    differences, reachEnd = sequence_of_differences(history)

    if reachEnd:
        return history[0]   
       
    prev = history[0] - predict_prev(differences)
    return prev

def test_predictPrev():
    assert predict_prev([3, 3, 3, 3, 3]) == 3
    assert predict_prev([0, 3, 6, 9, 12, 15]) == -3
    assert predict_prev([1, 3, 6, 10, 15, 21]) == 0


def read_file(lines):      
    histories = []
    for i, line in enumerate(lines):
        history = []
        
        lineNumbers = line.split(" ")
        for lineNumber in lineNumbers:
            history.append(int(lineNumber))

        histories.append(history)
    return histories


def test_day9_part1():
    with open('day9/test_input.txt', 'r') as file:
        histories = read_file(file.readlines())

    assert histories[0] == [0, 3, 6, 9, 12, 15]
    assert histories[1] == [1, 3, 6, 10, 15, 21]
    assert histories[2] == [10, 13, 16, 21, 30, 45]

    sum = 0
    for history in histories:
        sum += predict_prev(history)

    assert sum == 2


# Main Code
with open('day9/input.txt', 'r') as file:
    histories = read_file(file.readlines())
    
    sum = 0
    for history in histories:
        sum += predict_prev(history)

    print("Sum: ", sum)