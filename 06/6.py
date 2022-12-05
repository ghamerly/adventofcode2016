#!/usr/bin/env python3

# https://adventofcode.com/2016/day/6 - "Signals and Noise"
# Author: Greg Hamerly

import sys

first = lambda x: x[0]
second = lambda x: x[1]

def part1(counts):
    return ''.join(map(first, [max(c.items(), key=second) for c in counts]))

def part2(counts):
    return ''.join(map(first, [min(c.items(), key=second) for c in counts]))

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = list(map(str.strip, f))

    columns = list(zip(*lines))
    counts = [{c: col.count(c) for c in col} for col in columns]

    print('part 1:', part1(counts))
    print('part 2:', part2(counts))

if __name__ == '__main__':
    main()
