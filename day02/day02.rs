fn get_input() -> Vec<String> {
    let mut directions: Vec<String> = Vec::new();
    std::fs::read_to_string("day02.txt")
        .expect("file not found!")
        .lines()
        .for_each(|x| directions.push(x.to_string()));

    return directions;
}

fn part1() {
    let directions: Vec<String> = get_input();

    let mut x = 0;
    let mut y = 0;

    for direction in directions {
        let split = direction.split(" ");
        let vec: Vec<&str> = split.collect();
        let number = vec[1].parse::<usize>().unwrap();

        if direction.contains("forward") {
            x += number;
        } else if direction.contains("up") {
            y -= number;
        } else {
            y += number;
        }
    }

    println!("Part 1 solution: {}", x*y);
}

fn part2() {
    let directions: Vec<String> = get_input();

    let mut x = 0;
    let mut y = 0;
    let mut aim = 0;

    for direction in directions {
        let split = direction.split(" ");
        let vec: Vec<&str> = split.collect();
        let number = vec[1].parse::<usize>().unwrap();

        if direction.contains("forward") {
            x += number;
            y += aim*number;
        } else if direction.contains("up") {
            aim -= number;
        } else {
            aim += number;
        }
    }

    println!("Part 2 solution: {}", x*y);
}

fn main() {
    part1();
    part2();
}