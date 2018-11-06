#! /usr/bin/env python3

import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    'bill',
    help='Total amount of the bill.',
    type=int
)
parser.add_argument(
    'howmany',
    help='How many people split the bill.',
    type=int
)
args = parser.parse_args()

print(args.bill / args.howmany)
