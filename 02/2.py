#!/usr/bin/env python3

# https://adventofcode.com/2016/day/2 - "Bathroom Security"
# Author: Greg Hamerly

import sys

grid_p1 = [
        '00000',
        '01230',
        '04560',
        '07890',
        '00000',
        ]

grid_p2 = [
        '0000000',
        '0001000',
        '0023400',
        '0567890',
        '00ABC00',
        '000D000',
        '0000000',
        ]


direction = {
        'U': (-1,  0),
        'D': ( 1,  0),
        'L': ( 0, -1),
        'R': ( 0,  1)
        }

def simulate(commands, grid, r, c):
    password = []
    for line in commands:
        for d in line:
            dr, dc = direction[d]
            if grid[r + dr][c + dc] != '0':
                r += dr
                c += dc
        password.append(grid[r][c])
    return ''.join(password)

def part1(commands):
    return simulate(commands, grid_p1, 2, 2)

def part2(commands):
    return simulate(commands, grid_p2, 3, 1)

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = list(map(str.strip, f))

    print('part 1:', part1(lines))
    print('part 2:', part2(lines))

if __name__ == '__main__':
    main()
