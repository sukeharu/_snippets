#! /usr/bin/env python3

"""
argparse
see: https://docs.python.org/ja/3/howto/argparse.html
"""

import argparse

# set command line arguments - required
parser = argparse.ArgumentParser()

# positional argument
parser.add_argument(
    'x',
    help='base',
    type=int
)
parser.add_argument(
    'y',
    help='exponent',
    type=int
)

# optional argument
""" flag argument
parser.add_argument(
    '-v',
    '--verbose',
    help='increase output verbosity',
    action='store_true'  # flag
)
"""

# optional argument, it has choices 0, 1, 2
parser.add_argument(
    '-v',
    '--verbose',
    help='increase output verbosity',
    type=int,
    choices=[0, 1, 2]
)

# parse arguments - required
args = parser.parse_args()

# output
answer = args.x**args.y
if args.verbose == 2:
    print('Running: "{}"'.format(__file__))
elif args.verbose == 1:
    print('{}^{} == {}'.format(args.x, args.y, answer))
else:
    print(answer)
