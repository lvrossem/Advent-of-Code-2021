lines = list()

with open('day15.txt', 'r') as infile:
    for line in infile:
        lines.append([int(i) for i in line.strip()])


def part1():
    width = len(lines[0])
    height = len(lines)

    grid = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(1, width):
        grid[0][i] = sum(lines[0][1:i+1])

    for i in range(1, height):
        for j in range(width):
            if j == 0:
                grid[i][j] = grid[i-1][j] + lines[i][j]
            else:
                grid[i][j] = min(grid[i-1][j] + lines[i][j], grid[i][j-1] + lines[i][j])

    print(f'Solution for part 1 is {grid[-1][-1]}')


def part2():
    width = len(lines[0])
    height = len(lines)

    lines_extended = [[0 for _ in range(width * 5)] for _ in range(height * 5)]

    def copy_matrix(start, increment):
        y, x = start
        for i in range(y, y + height):
            for j in range(x, x + width):
                new_val = lines[i % height][j % width] + increment
                lines_extended[i][j] = new_val if new_val < 10 else (new_val % 10) + 1

    for i in range(5):
        for j in range(5):
            copy_matrix((i*height, j*width), i + j)
    
    grid = [[0 for _ in range(width*5)] for _ in range(height*5)]

    for i in range(1, width*5):
        grid[0][i] = grid[0][i-1] + lines_extended[0][i]

    for i in range(1, height*5):
        grid[i][0] = grid[i-1][0] + lines_extended[i][0]

    for i in range(1, height*5):
        for j in range(1, width*5):
            if j == 0:
                grid[i][j] = grid[i-1][j] + lines_extended[i][j]
            else:
                grid[i][j] = min(grid[i-1][j] + lines_extended[i][j], grid[i][j-1] + lines_extended[i][j])

    temp_solution = grid[-1][-1]
    stable = False

    while not stable:
        for i in range(1, height*5):
            for j in range(1, width*5):
                min_list = [grid[i-1][j] + lines_extended[i][j], grid[i][j-1] + lines_extended[i][j]]
                if j < width*5 - 1:
                    min_list.append(grid[i][j + 1] + lines_extended[i][j])
                if i < height*5 - 1:
                    min_list.append(grid[i + 1][j] + lines_extended[i][j])
                grid[i][j] = min(min_list)
        stable = temp_solution == grid[-1][-1]
        temp_solution = grid[-1][-1]

    
    print(f'Solution for part 2 is {grid[-1][-1]}')

part1()
part2()