use std::fs;

fn main() {
    part2();
    ()
}

fn part1() {
    let contents = fs::read_to_string("resource/input")
        .expect("Something went wrong");
    
    let mut cnt = 0;

    println!("Hello, world!");
    println!("Ay:\n{}", contents);

    for c in contents.chars() {
        if c == '(' {
            cnt += 1;
        } else {
            cnt -= 1;
        }
    }

    println!("Sol:\n{}", cnt);
    
}

fn part2() {
    let contents = fs::read_to_string("resource/input")
        .expect("Something went wrong");
    
    let mut cnt = 0;
    let mut pos = 0;

    println!("Hello, world!");
    println!("Ay:\n{}", contents);

    for c in contents.chars() {
        pos += 1;
        if c == '(' {
            cnt += 1;
        } else {
            cnt -= 1;
            if cnt < 0 {
                break
            }
        }
    }

    println!("Sol:\n{}", pos);
    
}
