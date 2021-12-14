from collections import defaultdict

chars = set()

def get_input():
    template = None
    rules = dict()
    with open('day14.txt') as infile:
        lines = infile.readlines()
        template = lines[0].strip()

        for line in lines[2:]:
            rule = line.strip().split(' -> ')
            rules[rule[0]] = rule[1]
            chars.add(rule[1])
    return template, rules


def solve(template, rules, iterations):

    string_counter = defaultdict(lambda: 0)
    char_counter = defaultdict(lambda: 0)

    for char in template:
        char_counter[char] += 1

    for char1 in chars:
        for char2 in chars:
            string_counter[char1+char2] = 0

    for i in range(len(template) - 1):
        string_counter[template[i] + template[i+1]] += 1

    for _ in range(iterations):
        new_counter = defaultdict(lambda: 0)
        for pair in string_counter:
            amount = string_counter[pair]
            if amount > 0:
                inserted = rules[pair]
                new_counter[pair[0] + inserted] += amount
                new_counter[inserted + pair[1]] += amount
                char_counter[inserted] += amount

        string_counter = new_counter
    
    min_value = char_counter[min(char_counter, key=char_counter.get)]
    max_value = char_counter[max(char_counter, key=char_counter.get)]

    return max_value - min_value
    
    print(f'Solution for part 1 is {max_value - min_value}')


def part1():
    template, rules = get_input()
    print(f'Solution for part 1 is {solve(template, rules, 10)}')


def part2():
    template, rules = get_input()
    print(f'Solution for part 2 is {solve(template, rules, 40)}')


part1()
part2()