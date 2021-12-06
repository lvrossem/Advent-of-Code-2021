def get_input():
    states = list()
    with open('day06.txt', 'r') as inputfile:
        for line in inputfile:
            states.extend([int(i) for i in line.split(',')])
    return states


def get_start_states():
    states = get_input()
    state_list = list()
    for i in range(9):
        state_list.append(states.count(i))

    return state_list


def iterate(states, iterations):
    for _ in range(iterations):
        states = [
            states[1],
            states[2],
            states[3],
            states[4],
            states[5],
            states[6],
            states[7] + states[0],
            states[8],
            states[0],
        ]

    return sum(states)

    
def part1():
    states = get_start_states()

    print(f'Solution for part 1 is {iterate(states, 80)}')


def part2():
    states = get_start_states()

    print(f'Solution for part 2 is {iterate(states, 256)}')


part1()
part2()