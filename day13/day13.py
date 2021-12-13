def print_lines(lines):
    for line in lines:
        for idx in range(len(line)):
            bool = line[idx]
            if bool:
                print('# ', end='')
            else:
                print('. ', end='')

            if idx == len(line) - 1:
                print('')
        
    print('\n')


def get_input():
    coords = list()
    instructions = list()

    with open('day13.txt', 'r') as infile:
        at_instructions = False
        for line in infile:
            if len(line) < 2:
                at_instructions = True
            else:
                if not at_instructions:
                    coord = [int(i) for i in line.strip().split(',')]
                    coords.append((coord[0], coord[1]))
                else:
                    instruction = line.strip().split('=')
                    instructions.append((instruction[0][-1], int(instruction[1])))
    
    max_x = max(coords, key=lambda x: x[0])[0]
    max_y = max(coords, key=lambda x: x[1])[1]

    lines = [[False for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in coords:
        lines[y][x] = True

    return lines, instructions


def fold(lines, instructions):
    lines_len = len(lines)
    line_len = len(lines[0])

    for instruction in instructions:
        mirror_coord = instruction[1]
        if instruction[0] == 'x':
            new_line_len = line_len - 1 - min(mirror_coord, line_len - 1 - mirror_coord)
            copy_length = min(line_len - mirror_coord - 1, mirror_coord)

            new_lines = [[False for _ in range(new_line_len)] for _ in range(lines_len)]

            for i in range(copy_length):
                for j in range(lines_len):
                    new_lines[j][new_line_len - 1 - i] = lines[j][mirror_coord + i + 1] or lines[j][mirror_coord - i - 1]

            for i in range(new_line_len - copy_length):
                for j in range(lines_len):
                    new_lines[j][i] = lines[j][i]

            line_len = new_line_len
            lines = new_lines

        else:
            new_lines_len = lines_len - 1 - min(mirror_coord, lines_len - 1 - mirror_coord)
            copy_length = min(lines_len - mirror_coord - 1, mirror_coord)

            new_lines = [[False for _ in range(line_len)] for _ in range(new_lines_len)]

            for i in range(copy_length):
                for j in range(line_len):
                    new_lines[new_lines_len - 1 - i][j] = lines[mirror_coord + i + 1][j] or lines[mirror_coord - i - 1][j]

            for i in range(new_lines_len - copy_length):
                for j in range(line_len):
                    new_lines[i][j] = lines[i][j]

            lines_len = new_lines_len
            lines = new_lines
            

    return lines
    


def part1():
    
    lines, instructions = get_input()
    folded = fold(lines, instructions[:1])

    result = 0
    for line in folded:
        result += line.count(True)
    print(f'Solution for part 1 is {result}')
    

def part2():
    lines, instructions = get_input()
    folded = fold(lines, instructions)

    # Just read the solution, not gonna parse this
    print_lines(folded)


part1()
part2()        