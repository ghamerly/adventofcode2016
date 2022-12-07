#!/usr/bin/env python3

# https://adventofcode.com/2016/day/10 - "Balance Bots"
# Author: Greg Hamerly
#
# This is really ugly.

import re
import sys

# a regular expression to match any of the input lines, and capture the key
# information into capture groups, which we later turn into dictionaries
command_pattern = re.compile(
        '^(?:' + \
                'bot (?P<srcbot>[0-9]+) gives low to ' + \
                '(?:bot (?P<lowbot>[0-9]+)|output (?P<lowoutput>[0-9]+)) and high to ' + \
                '(?:bot (?P<highbot>[0-9]+)|output (?P<highoutput>[0-9]+))' + \
                '|' + \
                'value (?P<value>[0-9]+) goes to bot (?P<valuebot>[0-9]+)' + \
                ')')

def output_iter(d):
    '''Identify all the keys for output destinations in a command.'''
    for key in ['lowoutput', 'highoutput']:
        if d[key] is not None:
            yield d[key]

def bot_iter(d):
    '''Identify all the keys for bot destinations in a command.'''
    for key in ['srcbot', 'lowbot', 'highbot', 'valuebot']:
        if d[key] is not None:
            yield d[key]

def simulate(commands):
    '''Given 'commands', parse the data and identify which chips each bot and
    output end up holding. Do this in a breadth-first way: first pass all
    values that are directly given to bots, then repeatedly identify bots that
    have two chips and have them pass their chips on.'''

    # identify all the possible bots and outputs
    bots = {} # bot_id => list of chips
    outputs = {} # output_id => list of chips
    bot_cmds = {} # bot_id => dictionary from original command regex match
    for cmd in commands:
        if 'srcbot' in cmd:
            bot_cmds[cmd['srcbot']] = cmd
        for b in bot_iter(cmd):
            bots[b] = []
        for o in output_iter(cmd):
            outputs[o] = []

    # initialize the values that are given directly to bots
    for cmd in commands:
        v = cmd['value']
        if v is not None:
            bots[cmd['valuebot']].append(v)

    # identify any both that is ready to start
    frontier = [b for b in bots if len(bots[b]) == 2]

    # do breadth-first search
    while frontier:
        new_frontier = []
        for b in frontier:
            low, high = sorted(bots[b])

            # handle bots passing to other bots and outputs
            for dest, val, context in (('lowbot', low, bots), ('highbot', high, bots), 
                                       ('lowoutput', low, outputs), ('highoutput', high, outputs)):
                d = bot_cmds[b][dest]
                if d is not None:
                    context[d].append(val)
                    if id(context) == id(bots) and len(bots[d]) == 2:
                        new_frontier.append(d)

        frontier = new_frontier

    return bots, outputs

def part1(bots, outputs):
    # identify which bot had a specially identified pair of values
    for b in bots:
        if sorted(bots[b]) == [17, 61]:
            return b

def part2(bots, outputs):
    # identify the multiplication of the first three outputs
    return outputs[0][0] * outputs[1][0] * outputs[2][0]

def mogrify(line):
    '''Use regex to parse each line, turn into a dictionary, and turn each
    non-None value into an integer.'''
    m = command_pattern.match(line)
    assert m, line
    toint = lambda v: None if v is None else int(v)
    return {k: toint(v) for k, v in m.groupdict().items()}

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    commands = list(map(mogrify, lines))
    bots, outputs = simulate(commands)

    print('part 1:', part1(bots, outputs))
    print('part 2:', part2(bots, outputs))

if __name__ == '__main__':
    main()
