extern crate byte_strings;

use std::fs;
use std::cmp::min;
use std::cmp::max;
use ::byte_strings::concat_bytes;

fn main() {
    part1();
    ()
}

fn part1() {
    let mut inp = "yzbqklnj";
    let mut suffix = 0;
    while true {
        let mut guess = inp.to_owned() + &suffix.to_string();
        let digest = md5::compute(guess.as_bytes());
        let digest_hex = format!("{:x}", digest);
        if &digest_hex[0..6] == "000000" {
            println!("yay:{}", suffix);
            break;
        }
        suffix += 1;
    }
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
