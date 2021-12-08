unique_lengths = [2, 3, 4, 7]
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
number_segments = [
    [1, 2, 3, 5, 6, 7],
    [3, 6],
    [1, 3, 4, 5, 7],
    [1, 3, 4, 6, 7],
    [2, 3, 4, 6],
    [1, 2, 4, 6, 7],
    [1, 2, 4, 5, 6, 7],
    [1, 3, 6],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 6, 7],
]

def get_input():
    with open('day08.txt', 'r') as inputfile:
        signal_patterns = list()
        for line in inputfile:
            split_line = line.split(' | ')
            signal_patterns.append(([pattern.strip() for pattern in split_line[0].split(' ')], [pattern.strip() for pattern in split_line[1].split(' ')]))
            
    return signal_patterns


def part1():
    patterns = get_input()
    result = 0

    for line in patterns:
        for pattern in line[1]:
            if len(pattern) in unique_lengths:
                result += 1

    print(f'Solution for part 1 is {result}')


def part2():
    patterns = get_input()
    result = 0
    for line in patterns:
        segment_signal_mapping = [set() for _ in range(8)]
        signals = line[0]
        numbers = line[1][::-1]
        
        signal_length_2 = set([signal for signal in signals if len(signal) == 2][0])
        signal_length_3 = set([signal for signal in signals if len(signal) == 3][0])

        segment_signal_mapping[1] = signal_length_3.difference(signal_length_2)

        intersect_2_3 = signal_length_2.intersection(signal_length_3)

        segment_signal_mapping[3] = intersect_2_3.copy()
        segment_signal_mapping[6] = intersect_2_3.copy()

        signals_length_6 = [set(signal) for signal in signals if len(signal) == 6]
        total_intersect = set.intersection(*signals_length_6)

        segment_signal_mapping[6] = total_intersect.intersection(segment_signal_mapping[6])
        segment_signal_mapping[3] = segment_signal_mapping[3].difference(segment_signal_mapping[6])

        remaining_intersect = total_intersect.difference(segment_signal_mapping[6], segment_signal_mapping[3], segment_signal_mapping[1])
        segment_signal_mapping[2] = remaining_intersect.copy()
        segment_signal_mapping[7] = remaining_intersect.copy()

        two_of_three = set()

        for char in char_list:
            if [char in s.difference(segment_signal_mapping[6], segment_signal_mapping[3], segment_signal_mapping[1]) for s in signals_length_6].count(True) == 2:
                two_of_three.add(char)

        segment_signal_mapping[4] = two_of_three.copy()
        segment_signal_mapping[5] = two_of_three.copy()


        signals_length_5 = [set(signal) for signal in signals if len(signal) == 5]
        total_intersect = set.intersection(*signals_length_5)

        segment_signal_mapping[4] = total_intersect.intersection(segment_signal_mapping[4])
        segment_signal_mapping[5] = segment_signal_mapping[5].difference(segment_signal_mapping[4])

        segment_signal_mapping[7] = total_intersect.intersection(segment_signal_mapping[7])
        segment_signal_mapping[2] = segment_signal_mapping[2].difference(segment_signal_mapping[7])

        segment_signal_mapping = [list(s)[0] for s in segment_signal_mapping[1:]]
        segment_signal_mapping = {segment_signal_mapping[i]: i+1 for i in range(7)}


        for i in range(len(numbers)):
            result += number_segments.index(sorted([segment_signal_mapping[char] for char in numbers[i]])) * 10 ** i

    print(f'Solution for part 2 is {result}')


part1()
part2()