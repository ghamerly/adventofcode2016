#!/usr/bin/env python3

# https://adventofcode.com/2016/day/5 - "How About a Nice Game of Chess?"
# Author: Greg Hamerly

import sys
import hashlib

def hash(key, i):
    s = key + str(i)
    h = hashlib.md5()
    h.update(s.encode('ascii'))
    h = h.hexdigest()
    if h.startswith('00000'):
        return h[5:7]
    return None

def part1(data):
    key = data[0]
    password = []

    i = 0
    while len(password) < 8:
        h = hash(key, i)
        if h is not None:
            password.append(h[0])
        i += 1

    return ''.join(password)

def part2(data):
    key = data[0]
    password = ['-'] * 8

    i = 0
    while '-' in password:
        h = hash(key, i)
        if h is not None:
            try:
                pos = int(h[0])
                if password[pos] == '-':
                    password[pos] = h[1]
            except:
                pass
        i += 1

    return ''.join(password)


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
