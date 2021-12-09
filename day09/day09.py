lines = list()
with open('day09.txt', 'r') as inputfile:
    for line in inputfile:
        lines.append([int(i) for i in line.strip()])

lines_len = len(lines)
line_len = len(lines[0])

def get_lowpoints():
    lowpoints = set()

    for i in range(lines_len):
        for j in range(line_len):
            depth = lines[i][j]
            smaller = list()
            if i > 0:
                smaller.append(depth < lines[i-1][j])
            if i < lines_len - 1:
                smaller.append(depth < lines[i+1][j])
            if j > 0:
                smaller.append(depth < lines[i][j-1])
            if j < line_len - 1:
                smaller.append(depth < lines[i][j+1])

            if all(smaller):
                lowpoints.add((i, j))

    return lowpoints


def part1():
    result = 0

    for y, x in get_lowpoints():
        result += lines[y][x] + 1

    print(f'Solution for part 1 is {result}')


def recursive_flood(coord, basin):
    y, x = coord

    if y < lines_len - 1 and lines[y+1][x] > lines[y][x] and lines[y+1][x] != 9:
        basin.add((y+1, x))
        recursive_flood((y+1, x), basin)
    if y > 0 and lines[y-1][x] > lines[y][x] and lines[y-1][x] != 9:
        basin.add((y-1, x))
        recursive_flood((y-1, x), basin)
    if x < line_len - 1 and lines[y][x+1] > lines[y][x] and lines[y][x+1] != 9:
        basin.add((y, x+1))
        recursive_flood((y, x+1), basin)
    if x > 0 and lines[y][x-1] > lines[y][x] and lines[y][x-1] != 9:
        basin.add((y, x-1))
        recursive_flood((y, x-1), basin)

def part2():
    basins = list()

    for y, x in get_lowpoints():
        basin = {(y, x)}
        recursive_flood((y, x), basin)
        basins.append(basin)

    three_largest = sorted(basins, key=lambda x: len(x))[len(basins) - 3:]
    result = len(three_largest[0]) * len(three_largest[1]) * len(three_largest[2])

    print(f'Solution for part 2 is {result}')
            

part1()
part2()