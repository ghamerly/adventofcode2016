#!/usr/bin/env python3

# https://adventofcode.com/2016/day/3 - "Squares With Three Sides"
# Author: Greg Hamerly

import sys

def part1(data):
    possible = 0
    for a, b, c in data:
        m = max(a, b, c)
        if 2 * m < a + b + c:
            possible += 1
    return possible

def part2(data):
    possible = 0
    for row in range(0, len(data), 3):
        for col in range(3):
            a, b, c = data[row][col], data[row+1][col], data[row+2][col]
            m = max(a, b, c)
            if 2 * m < a + b + c:
                possible += 1
    return possible

def mogrify(line):
    return list(map(int, line.split()))

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = list(map(str.strip, f))

    data = list(map(mogrify, lines))

    print('part 1:', part1(data))
    print('part 2:', part2(data))

if __name__ == '__main__':
    main()
