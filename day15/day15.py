lines = list()

with open('day15.txt', 'r') as infile:
    for line in infile:
        lines.append([int(i) for i in line.strip()])

width = len(lines[0])
height = len(lines)


def get_min_risk(risks, height, width):
    grid = [[float('inf') for _ in range(width)] for _ in range(height)]

    grid[0][0] = 0
    for i in range(1, width):
        grid[0][i] = grid[0][i-1] + risks[0][i]

    for i in range(1, height):
        grid[i][0] = grid[i-1][0] + risks[i][0]

    solution = grid[-1][-1]
    stable = False

    while not stable:
        for i in range(1, height):
            for j in range(1, width):
                min_list = [grid[i-1][j] + risks[i][j], grid[i][j-1] + risks[i][j]]
                if j < width - 1:
                    min_list.append(grid[i][j + 1] + risks[i][j])
                if i < height - 1:
                    min_list.append(grid[i + 1][j] + risks[i][j])
                grid[i][j] = min(min_list)

        stable = solution == grid[-1][-1]
        solution = grid[-1][-1]

    return solution


def part1():
    result = get_min_risk(lines, height, width)
    print(f'Solution for part 1 is {result}')


def part2():
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
    
    result = get_min_risk(lines_extended, height*5, width*5)

    print(f'Solution for part 2 is {result}')

part1()
part2()