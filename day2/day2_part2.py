import re
import pytest

def maxValues(line):
    red = 0
    green = 0
    blue = 0

    itterations = line.split(';')

    for itteration in itterations:
         colors = itteration.split(',')
         for color in colors:
            number = int(re.findall(r'\d+', color)[0])
            if color.find("red") != -1 and number > red:
                red = number
            if color.find("green") != -1 and number > green:
                green = number
            if color.find("blue") != -1 and number > blue:
                blue = number   

    return red, green, blue

def test_maxValues():
    red, green, blue = maxValues(" 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert red == 4
    assert green == 2
    assert blue == 6
    red, green, blue = maxValues("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert red == 20
    assert green == 13
    assert blue == 6  
     
def test_input_day2():
    with open('day2/test_input_day2.txt', 'r') as file:        
        sum= 0
        for line in file:
            print(line.strip()) 
            parts = line.split(':')
            red, green, blue = maxValues(parts[1])
            print("red : ",red, ", green: ", green, ", blue: ", blue)  
            power = red * green * blue
            print("power : ",power)

            sum += power
                
        print("sum : ", sum)
        assert sum == 2286

# Main program starts here
with open('day2/input_day2.txt', 'r') as file:

    sum = 0

    for line in file: 
        parts = line.split(':')
        red, green, blue = maxValues(parts[1])
        power = red * green * blue
        sum += power
            
    print("sum : ",sum)





