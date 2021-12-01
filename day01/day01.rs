fn main() {
    let mut numbers: Vec<usize> = Vec::new();
    std::fs::read_to_string("day01.txt")
        .expect("file not found!")
        .lines()
        .for_each(|x| numbers.push(x.parse::<usize>().unwrap()));

    let mut result = 0;

    for i in 1..numbers.len() {
        if numbers[i] > numbers[i - 1] {
            result += 1;
        }
    }

    println!("Result for day 1 is {}", result);

    result = 0;

    let mut previous_sum = numbers[0] + numbers[1] + numbers[2];

    for i in 1..numbers.len() - 2 {
        let new_sum = previous_sum - numbers[i - 1] + numbers[i + 2];

        if new_sum > previous_sum {
            result += 1;
        }

        previous_sum = new_sum;
    }

    println!("Result for day 2 is {}", result);
}