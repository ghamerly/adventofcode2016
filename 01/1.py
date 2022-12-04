#!/usr/bin/env python3

# https://adventofcode.com/2016/day/1 - "No Time for a Taxicab"
# Author: Greg Hamerly

import sys

def turn(current_direction, turn_direction):
    if current_direction == 'NORTH':
        if turn_direction == 'L':
            return 'WEST'
        return 'EAST'
    elif current_direction == 'EAST':
        if turn_direction == 'L':
            return 'NORTH'
        return 'SOUTH'
    elif current_direction == 'SOUTH':
        if turn_direction == 'L':
            return 'EAST'
        return 'WEST'
    elif current_direction == 'WEST':
        if turn_direction == 'L':
            return 'SOUTH'
        return 'NORTH'

def part1(commands):
    direction = 'NORTH'
    x = y = 0

    for c in commands:
        turn_direction = c[0]
        direction = turn(direction, turn_direction)
        steps = int(c[1:])

        if direction == 'NORTH':
            y = y + steps
        elif direction == 'SOUTH':
            y = y - steps
        elif direction == 'EAST':
            x = x + steps
        elif direction == 'WEST':
            x = x - steps

    return abs(x) + abs(y)

def part2(commands):
    direction = 'NORTH'
    x = y = 0

    locations = {(0, 0)}

    for c in commands:
        turn_direction = c[0]
        direction = turn(direction, turn_direction)
        steps = int(c[1:])

        dx = dy = 0
        if direction == 'NORTH':
            dy = 1
        elif direction == 'SOUTH':
            dy = -1
        elif direction == 'EAST':
            dx = 1
        elif direction == 'WEST':
            dx = -1

        for i in range(1, steps + 1):
            x += dx
            y += dy
            if (x, y) in locations:
                return abs(x) + abs(y)
            locations.add((x, y))

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = list(map(str.strip, f))

    commands = lines[0].split(', ')

    print('part 1:', part1(commands))
    print('part 2:', part2(commands))

if __name__ == '__main__':
    main()
