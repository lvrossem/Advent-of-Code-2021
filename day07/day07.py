
from sys import maxsize

def get_input():
    with open('day07.txt', 'r') as inputfile:
        line = inputfile.readline()
        return [int(i) for i in line.split(',')]

    
def part1():
    positions, min_fuel = get_input(), maxsize
    for align_x in range(max(positions)):
        fuel = sum([abs(align_x - x) for x in positions])
        if fuel < min_fuel:
            min_fuel = fuel
    print(f'Solution for part 1 is {min_fuel}')


def part2():
    positions, min_fuel = get_input(), maxsize
    for align_x in range(max(positions)):
        fuel = sum([(abs(align_x - x) + abs(align_x - x) ** 2) / 2 for x in positions])
        if fuel < min_fuel:
            min_fuel = fuel
    print(f'Solution for part 2 is {min_fuel}')


part1()
part2()