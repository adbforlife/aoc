use std::fs;
use std::cmp::min;
use std::cmp::max;
use std::collections::HashSet;

fn main() {
    part2();
    ()
}

fn part1() {
    let mut h: HashSet<(i32, i32)> = vec![(0,0)].into_iter().collect();
    let mut contents = fs::read_to_string("input")
        .expect("Something went wrong");
    let mut pos = (0,0);
    for c in contents.trim().chars() {
        if c == '<' {
            pos = (pos.0 - 1, pos.1);
            h.insert(pos);
        } else if c == '>' {
            pos = (pos.0 + 1, pos.1);
            h.insert(pos);
        } else if c == 'v' {
            pos = (pos.0, pos.1 - 1);
            h.insert(pos);
        } else if c == '^' {
            pos = (pos.0, pos.1 + 1);
            h.insert(pos);
        }
    }
    println!("len:{}", h.len());
     
}

fn part2() {
    let mut h1: HashSet<(i32, i32)> = vec![(0,0)].into_iter().collect();
    let mut h2: HashSet<(i32, i32)> = vec![(0,0)].into_iter().collect();
    let mut contents = fs::read_to_string("input")
        .expect("Something went wrong");
    let mut pos1 = (0,0);
    let mut pos2 = (0,0);
    for (i,c) in contents.trim().chars().enumerate() {
        if c == '<' {
            if i % 2 == 0 {
                pos1.0 -= 1;
                h1.insert(pos1);
            } else {
                pos2 = (pos2.0 - 1, pos2.1);
                h2.insert(pos2);
            }
        } else if c == '>' {
            if i % 2 == 0 {
                pos1 = (pos1.0 + 1, pos1.1);
                h1.insert(pos1);
            } else {
                pos2 = (pos2.0 + 1, pos2.1);
                h2.insert(pos2);
            }
        } else if c == 'v' {
            if i % 2 == 0 {
                pos1 = (pos1.0, pos1.1 - 1);
                h1.insert(pos1);
            } else {
                pos2 = (pos2.0, pos2.1 - 1);
                h2.insert(pos2);
            }
        } else if c == '^' {
            if i % 2 == 0 {
                pos1 = (pos1.0, pos1.1 + 1);
                h1.insert(pos1);
            } else {
                pos2 = (pos2.0, pos2.1 + 1);
                h2.insert(pos2);
            }
        }
    }
    let mut cnt = 0;
    for a in h1.union(&h2) {
        cnt += 1;
    }
    println!("len:{}", cnt);

    
}
