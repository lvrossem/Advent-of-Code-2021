neighbors = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
flashes = 0


def get_input():
    lines = list()
    with open('day11.txt', 'r') as infile:
        for line in infile:
            lines.append([int(i) for i in line.strip()])
    return lines


def flash_recursive(lines, flashed, y, x):
    lines_len = len(lines)
    line_len = len(lines[0])

    valid_neighbors = set()
    for y_dir, x_dir in neighbors:
        new_y, new_x = y + y_dir, x + x_dir
        if 0 <= new_y < lines_len and 0 <= new_x < line_len:
            lines[new_y][new_x] += 1
            valid_neighbors.add((new_y, new_x))

    for new_y, new_x in valid_neighbors:
        if lines[new_y][new_x] > 9 and (new_y, new_x) not in flashed:
            flashed.add((new_y, new_x))
            global flashes
            flashes += 1
            flash_recursive(lines, flashed, new_y, new_x)


def part1():
    lines = get_input()
    lines_len = len(lines)
    line_len = len(lines[0])

    for i in range(100):
        flashed = set()
        for y in range(lines_len):
            for x in range(line_len):
                lines[y][x] += 1
    
        for y in range(lines_len):
            for x in range(line_len):
                if lines[y][x] > 9 and (y, x) not in flashed:
                    
                    global flashes
                    flashes += 1
                    flashed.add((y, x))
                    flash_recursive(lines, flashed, y, x)
                    
        for y, x in flashed:
            lines[y][x] = 0

    print(f'Solution for part 1 is {flashes}')


def part2():
    lines = get_input()
    lines_len = len(lines)
    line_len = len(lines[0])

    complete = False
    step = 0

    while not complete:
        step += 1
        flashed = set()
        for y in range(lines_len):
            for x in range(line_len):
                lines[y][x] += 1
    
        for y in range(lines_len):
            for x in range(line_len):
                if lines[y][x] > 9 and (y, x) not in flashed:
                    flashed.add((y, x))
                    flash_recursive(lines, flashed, y, x)
                    
        for y, x in flashed:
            lines[y][x] = 0

        complete = len(flashed) == 100


    print(f'Solution for part 2 is {step}')


part1()
part2()