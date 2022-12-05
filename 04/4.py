#!/usr/bin/env python3

# https://adventofcode.com/2016/day/4 - "Security Through Obscurity"
# Author: Greg Hamerly

import sys

def is_valid_room(name, checksum):
    count = {c: name.count(c) for c in name if c != '-'}
    ordered = sorted((-cnt, char) for char, cnt in count.items())
    for (cnt, char), chk in zip(ordered, checksum):
        if char != chk:
            return False
    return True

def part1(data):
    sector_sum = 0

    for name, sector, checksum in data:
        if is_valid_room(name, checksum):
            sector_sum += sector

    return sector_sum

def part2(data):
    a = ord('a')
    shift = lambda c, dist: ' ' if c == '-' else chr((ord(c) - a + dist) % 26 + a)
    for name, sector, checksum in data:
        if is_valid_room(name, checksum):
            decrypted = ''.join([shift(c, sector) for c in name])
            if 'northpole' in decrypted:
                return sector

def mogrify(line):
    a, checksum = line.strip(']').split('[')
    parts = a.split('-')
    name = '-'.join(parts[:-1])
    sector = parts[-1]
    return name, int(sector), checksum

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
