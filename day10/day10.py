lines = list()
with open('day10.txt', 'r') as infile:
    for line in infile:
        lines.append(line.strip())

openers = ['(', '{', '<', '[']
closers = [')', '}', '>', ']']

rewards1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

rewards2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def get_score(completion):
    score = 0
    for char in completion:
        score = score * 5 + rewards2[char]
    return score


def part1():
    result = 0
    for line in lines:
        index = 0
        stack = list()
        while index < len(line):
            char = line[index]
            if char in openers:
                stack.append(char)
            else:
                opener = stack.pop()
                if opener != openers[closers.index(char)]:
                    result += rewards1[char]
                    index = len(line)
            index += 1
    
    print(f'Solution for part 1 is {result}')


def part2():
    result = list()
    for line in lines:
        corrupt = False
        index = 0
        stack = list()
        while index < len(line):
            char = line[index]
            if char in openers:
                stack.append(char)
            else:
                opener = stack.pop()
                if opener != openers[closers.index(char)]:
                    index = len(line)
                    corrupt = True
            index += 1

        if not corrupt:
            completion = [closers[openers.index(char)] for char in stack[::-1]]
            result.append(get_score(completion))
            
    print(f'Solution for part 2 is {sorted(result)[int(len(result) / 2)]}')


part1()
part2()