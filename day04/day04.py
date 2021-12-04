def get_input():
    inputfile = open('day04.txt', 'r')
    lines = inputfile.readlines()

    pulled_numbers = [int(i) for i in lines[0].split(',')]
    grids = list()

    current_grid = list()
    for line_nr in range(1, len(lines)):
        line = lines[line_nr]
        if len(line) < 2:
            if len(current_grid) > 0:
                grids.append(current_grid[:])
            current_grid = list()
        else:
            current_grid.append([(int(i), False) for i in line.rstrip().split()])

    grids.append(current_grid)

    return pulled_numbers, grids


def sum_non_marked(grid):
    result = 0
    for row in grid:
        for entry in row:
            if not entry[1]:
                result += entry[0]
    return result


def check_win(grid, pulled_number):
    for row in grid:
        if all([row[i][1] for i in range(len(row))]):
            return sum_non_marked(grid) * pulled_number

    for col_nr in range(len(grid[0])):
        if all([grid[i][col_nr][1] for i in range(len(grid))]):
            return sum_non_marked(grid) * pulled_number

    return 0


def apply_pulled_numbers(grids, pulled_number, part2=False):
    won_grids = list()

    for grid_index in range(len(grids)):
        grid = grids[grid_index]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x][0] == pulled_number:
                    grid[y][x] = (pulled_number, True)
        
        result = check_win(grid, pulled_number)
        if result > 0:
            if part2:
                won_grids.append(grid_index)
            else:
                return result, grid_index
    
    if part2:
        return won_grids
    else:
        return None, None


def part1():
    pulled_numbers, grids = get_input()

    pulled_number_index = 0
    won = False
    while not won:
        result, _ = apply_pulled_numbers(grids, pulled_numbers[pulled_number_index])
        
        if result is not None:
            won = True
            print(f'Solution for part 1: {result}')

        pulled_number_index += 1


def part2():
    pulled_numbers, grids = get_input()
    won_flags = [False for _ in grids]

    for pulled_number in pulled_numbers:
        won_grids = apply_pulled_numbers(grids, pulled_number, True)

        for index in won_grids:
            if won_flags.count(False) == 1:

                last_grid_index = won_flags.index(False)
                win_value = check_win(grids[last_grid_index], pulled_number)

                if win_value > 0:
                    print(f'Solution for part 2: {win_value}')
                    return 0
                    
            won_flags[index] = True
        

part1()
part2()