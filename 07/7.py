#!/usr/bin/env python3

# https://adventofcode.com/2016/day/7 - "Internet Protocol Version 7"
# Author: Greg Hamerly

import re
import sys

def find_inside_outside_groups(line):
    p = re.compile('(?P<outside>[a-z]+)|\[(?P<inside>[a-z]+)\]')
    insides = set()
    outsides = set()
    for m in p.finditer(line):
        inside, outside = m.group('inside'), m.group('outside')
        if inside:
            insides.add(inside)
        elif outside:
            outsides.add(outside)
        else:
            assert False, line

    return insides, outsides

def has_abba(s):
    for i in range(len(s) - 3):
        a, b = s[i:i+2], s[i+2:i+4]
        if a[0] == a[1]:
            continue
        if a == b[::-1]:
            return True
    return False

def find_abas(s):
    for i in range(len(s) - 2):
        si = s[i:i+3]
        if si[0] == si[2] and si[0] != si[1]:
            yield si

def supports_tls(line):
    insides, outsides = find_inside_outside_groups(line)
    return any(map(has_abba, outsides)) and not any(map(has_abba, insides))

def supports_ssl(line):
    insides, outsides = find_inside_outside_groups(line)

    f = lambda s: list(find_abas(s))
    inside_abas = set(sum(map(f, insides), []))
    outside_abas = sum(map(f, outsides), [])
    outside_babs = {f'{b}{a}{b}' for (a, b, c) in outside_abas}

    return bool(inside_abas & outside_babs)

def part1(data):
    return sum(map(supports_tls, data))

def part2(data):
    return sum(map(supports_ssl, data))

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    print('part 1:', part1(lines))
    print('part 2:', part2(lines))

if __name__ == '__main__':
    main()
