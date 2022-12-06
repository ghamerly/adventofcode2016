#!/usr/bin/env python3

# https://adventofcode.com/2016/day/9 - "Explosives in Cyberspace"
# Author: Greg Hamerly

import re
import sys

marker = re.compile('\(([0-9]+)x([0-9]+)\)')

def part1(line):
    result = []
    last = 0
    for m in marker.finditer(line):
        num, repeat = map(int, m.groups())
        start, end = m.span()
        if end <= last:
            continue
        result.append(line[last:start])
        result.append(line[end:end+num] * repeat)
        last = end + num

    result.append(line[last:])

    #print(''.join(result))
    return sum(map(len, result))

def parse(line, start, end, mult=1):
    '''Recursively parse the given line on the range [start,end).
    Keep track of the multipliers as we descend by multiplying them together.

    1. Find the first occurrence of a marker (if any).
    2. If there is no marker, just return the length of the substring
       (multiplied by mult).
    3. Otherwise, we found a marker. The answer is the length of the prefix
       (before the marker) multiplied by mult, plus the length of the
       recursively parsed string (multiplied by mult * repeat).
    4. If we still haven't finished parsing the string (the marker does not
       extend all the way to "end"), recursively parse again (with the multipler
       we were given).'''

    #print(f'parsing [{start},{end}): {line[start:end]}')
    m = marker.search(line, pos=start, endpos=end)
    if not m:
        #print(f'no markers, returning {end - start} * {mult} = {(end-start)*mult}')
        return (end - start) * mult

    num, repeat = map(int, m.groups())
    m_start, m_end = m.span()

    # the part of the string before the marker
    prefix_len = (m_start - start) * mult

    # everything the marker covers (with "repeat" multiplied in)
    recursive_len = parse(line, m_end, min(m_end + num, end), mult * repeat)
    ans = prefix_len + recursive_len

    # if the marker does not cover all the way to the end, parse further (with
    # the multiplier we were given)
    if m_end + num < end:
        ans += parse(line, m_end + num, end, mult)

    #print(f'[{start},{end}) returning {ans}')
    return ans

def part2(line):
    return parse(line, 0, len(line))

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]
    
    for i, line in enumerate(lines):
        print()
        print(f'line {i}: {line[:10]}...')
        print('part 1:', part1(line))
        print('part 2:', part2(line))

if __name__ == '__main__':
    main()
