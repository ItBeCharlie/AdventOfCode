use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let file_contents = fs::read_to_string("day1.in")?;
    // println!("{}", file_contents);
    let part1_sum: i32 = file_contents
        .lines()
        .map(|line| line.parse::<i32>().unwrap())
        .sum();
    println!("Sum: {}", part1_sum);

    let lines = file_contents.lines().cycle();
    let mut previous_values: Vec<i32> = vec![];
    let mut sum = 0;
    for line in lines {
        previous_values.push(sum);
        sum += line.parse::<i32>().unwrap();
        // println!("{:?}", previous_values);
        if previous_values.contains(&sum) {
            println!("Duplicate: {}", sum);
            break;
        }
    }
    // println!("Sum: {}", sum);
    Ok(())
}
