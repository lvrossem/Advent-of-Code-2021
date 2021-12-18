min_x, max_x, min_y, max_y = None, None, None, None

with open('day17.txt', 'r') as infile:
    line = infile.readline().strip()
    x = line.split(', ')[0].split('=')[1].split('..')
    y = line.split(', ')[1].split('=')[1].split('..')

    min_x, max_x = int(x[0]), int(x[1])
    min_y, max_y = int(y[0]), int(y[1])

print(f'{min_x}, {max_x}, {min_y}, {max_y}, ')
def part1():
    print(f'Solution for part 1 is {(-min_y - 1)*(-min_y)/2} ')


def new_x_vel(x_vel):
    if x_vel > 0:
        return x_vel - 1
    elif x_vel < 0:
        return x_vel + 1
    else:
        return 0


def part2():
    result = 0
    for i in range(max_x + 1):
        for j in range(min_y - 1, 1000):
            x_vel = i
            y_vel = j
            x, y = 0, 0

            hit = False

            while not x > max_x and not y < min_y and not hit:
                x += x_vel
                y += y_vel
                x_vel = new_x_vel(x_vel)
                y_vel -= 1

                hit = min_x <= x <= max_x and min_y <= y <= max_y
            if hit:
                result += 1

    print(f'Solution for part 2 is {result}')
part1()
part2()