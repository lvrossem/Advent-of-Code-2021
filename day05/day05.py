def get_input():
    with open('day05.txt', 'r') as inputfile:
        lines = list()
        for line in inputfile:
            coords = line.split(' -> ')
            coord1, coord2 = coords[0].split(','), coords[1].split(',')

            lines.append(((int(coord1[0]), int(coord1[1])), (int(coord2[0]), int(coord2[1]))))

    return lines


def get_dimensions(lines):
    max_x = max(max(lines, key=lambda x: x[0][0])[0][0], max(lines, key=lambda x: x[1][0])[1][0])

    max_y = max(max(lines, key=lambda x: x[0][1])[0][1], max(lines, key=lambda x: x[1][1])[1][1])

    return max_x + 1, max_y + 1


def get_grid(lines):
    width, height = get_dimensions(lines)
    return [[0 for _ in range(width + 1)] for _ in range(height + 1)]


def part1():
    lines = get_input()
    grid = get_grid(lines)

    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            min_y = min(line[0][1], line[1][1])
            max_y = max(line[0][1], line[1][1])

            min_x = min(line[0][0], line[1][0])
            max_x = max(line[0][0], line[1][0])
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    grid[y][x] += 1

    result = 0

    for line in grid:
        for number in line:
            if number > 1:
                result += 1

    print(f'Solution for part 1 is {result}')


def part2():
    lines = get_input()
    grid = get_grid(lines)

    for line in lines:
        x_incr = 1 if line[1][0] > line[0][0] else -1
        y_incr = 1 if line[1][1] > line[0][1] else -1

        if line[1][0] == line[0][0]:
            x_incr = 0

        if line[1][1] == line[0][1]:
            y_incr = 0

        x, y = line[0][0], line[0][1]

        while x != line[1][0] + x_incr or y != line[1][1] + y_incr:
            grid[y][x] += 1
            x += x_incr
            y += y_incr

    result = 0

    for line in grid:
        for number in line:
            if number > 1:
                result += 1

    print(f'Solution for part 2 is {result}')


part1()
part2()