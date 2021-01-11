use std::fs;
use std::cmp::min;
use std::cmp::max;

fn main() {
    part2();
    ()
}

fn part1() {
    let mut contents = fs::read_to_string("input")
        .expect("Something went wrong");

    let mut res = 0;

    for s in contents.trim().split("\n") {
        println!("s:{}\n", s);
        let mut nums: Vec<&str> = s.split("x").collect();
        let a = nums[0].parse::<i32>().unwrap();
        let b = nums[1].parse::<i32>().unwrap();
        let c = nums[2].parse::<i32>().unwrap();
        res += 2 * a * b + 2 * a * c + 2 * b * c + min(min(a*b,b*c), a*c);
    }
    println!("Res:{}\n", res);
    
}

fn part2() {
    let mut contents = fs::read_to_string("resource/input")
        .expect("Something went wrong");

    let mut res = 0;

    for s in contents.trim().split("\n") {
        println!("s:{}", s);
        let mut nums: Vec<&str> = s.split("x").collect();
        let a = nums[0].parse::<i32>().unwrap();
        let b = nums[1].parse::<i32>().unwrap();
        let c = nums[2].parse::<i32>().unwrap();
        res += a * b * c;
        res += 2 * (a + b + c);
        res -= 2 * max(max(a,b),c);
    }
    println!("Res:{}\n", res);
    
}
