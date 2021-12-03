use std::char;

fn get_input() -> Vec<String> {
    let mut directions: Vec<String> = Vec::new();
    std::fs::read_to_string("day03.txt")
        .expect("file not found!")
        .lines()
        .for_each(|x| directions.push(x.to_string()));

    return directions;
}

fn most_common_bit(input: &Vec<String>, position: usize) -> char {
    let input_length: usize = input.len();

    let mut zeroes = 0;

    for line_nr in 0..input_length {
        if input[line_nr].chars().nth(position).unwrap() == '0' {
            zeroes += 1
        }
    }

    if zeroes > input_length / 2 {
        return '0';
    } else {
        return '1';
    }
}

fn bitflip(bit: char) -> char {
    return char::from_digit((bit.to_digit(10).unwrap() + 1) % 2, 10).unwrap();
}

fn part1() {
    let input: Vec<String> = get_input();

    let number_length: usize = input[0].len();

    let mut gamma = 0;

    for position in 0..number_length {
        if most_common_bit(&input, position) == '1' {
            gamma |= 1 << (number_length - position - 1);
        }
    }

    let epsilon = (1 << number_length) - 1 - gamma;

    println!("Solution for part 1 is {}", gamma*epsilon);

}

fn part2() {
    let mut input: Vec<String> = get_input();
    let mut input_clone = input.clone();

    let number_length = input[0].len();

    let mut position = 0;

    while input.len() > 1 {
        let most_common = most_common_bit(&input, position);
        input = input.into_iter().filter(|s| s.chars().nth(position).unwrap() == most_common).collect();
        position = (position + 1) % number_length;
    }

    position = 0;

    while input_clone.len() > 1 {
        let least_common = bitflip(most_common_bit(&input_clone, position));
        input_clone = input_clone.into_iter().filter(|s| s.chars().nth(position).unwrap() == least_common).collect();
        position = (position + 1) % number_length;
    }

    let oxygen = isize::from_str_radix(&input[0], 2).unwrap();
    let co2 = isize::from_str_radix(&input_clone[0], 2).unwrap();

    println!("Solution for part 2 is {}", oxygen * co2);
}

fn main() {
    part1();
    part2();
}