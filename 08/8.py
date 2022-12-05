#!/usr/bin/env python3

# https://adventofcode.com/2016/day/8 - "Two-Factor Authentication"
# Author: Greg Hamerly

import re
import sys

def part1(commands):
    grid = [[' '] * 50 for _ in range(6)]
    #grid = [[' '] * 7 for _ in range(3)] # for sample.in
    for cmd in commands:
        cmd(grid)

    for row in grid:
        print(''.join(row))

    return sum([sum(map(lambda c: c == '#', row)) for row in grid])

def part2(data):
    return 'just read the letters above'

splitter = re.compile(' |=|([0-9]+)x([0-9]+)')

def rect(a, b):
    def f(grid):
        for row in range(b):
            for col in range(a):
                grid[row][col] = '#'
    return f

def rotate_y(a, b):
    def f(grid):
        n = len(grid[0])
        grid[a] = [grid[a][(i + n - b) % n] for i in range(n)]
    return f

def rotate_x(a, b):
    def f(grid):
        n = len(grid)
        r = [grid[(i + n - b) % n][a] for i in range(n)]
        for i in range(n):
            grid[i][a] = r[i]
    return f

def mogrify(line):
    parts = list(filter(None, splitter.split(line)))

    cmd = parts[0]
    if cmd == 'rect':
        a, b = map(int, parts[1:])
        return rect(a, b)

    a, b = int(parts[3]), int(parts[5])
    if parts[2] == 'y':
        return rotate_y(a, b)
    return rotate_x(a, b)

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    commands = list(map(mogrify, lines))

    print('part 1:', part1(commands))
    print('part 2:', part2(commands))

if __name__ == '__main__':
    main()
