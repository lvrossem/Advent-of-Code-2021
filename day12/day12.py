system = dict()
with open('day12.txt', 'r') as infile:
    for line in infile:
        caves = line.split('-')
        caves = [cave.strip() for cave in caves]
        if caves[0] not in system:
            system[caves[0]] = {caves[1]}
        else:
            system[caves[0]].add(caves[1])

        if caves[1] not in system:
            system[caves[1]] = {caves[0]}
        else:
            system[caves[1]].add(caves[0])


def search_recursive(current, visited):
    if current == 'end':
        visited.remove(current)
        return 1

    path_count = 0
    for neighbor in system[current]:
        if not neighbor.islower() or neighbor not in visited:
            if neighbor.islower():
                visited.add(neighbor)
            path_count += search_recursive(neighbor, visited)

    if current.islower():
        visited.remove(current)
    return path_count


def part1():
    current = 'start'
    visited = {'start'}
    result = 0

    for neighbor in system[current]:
        if neighbor.islower():
            visited.add(neighbor)
        result += search_recursive(neighbor, visited)

    print(f'Solution for part 1 is {result}')


def search_recursive2(current, visited):
    if current == 'end':
        visited.pop()
        return 1

    path_count = 0
    for neighbor in system[current]:
        if neighbor.isupper():
            path_count += search_recursive2(neighbor, visited)
        else:
            if neighbor != 'start':
                if neighbor in visited:
                    if len(set(visited)) == len(visited):
                        visited.append(neighbor)
                        path_count += search_recursive2(neighbor, visited)
                else:
                    visited.append(neighbor)
                    path_count += search_recursive2(neighbor, visited)
                
    if current.islower():
        visited.pop()
    return path_count


def part2():
    current = 'start'
    visited = ['start']
    result = 0

    for neighbor in system[current]:
        if neighbor.islower():
            visited.append(neighbor)
        result += search_recursive2(neighbor, visited)

    print(f'Solution for part 2 is {result}')


part1()
part2()