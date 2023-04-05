#!/usr/bin/python3
import sys

def factorize(b):
    """ Generate 2 factors for a given number"""
    f = 2
    while (b % f):
        if (f <= b):
            f += 1

    g = b // f
    return (g, f)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    b = int(line.rstrip())
    g, f = factorize(b)
    print(f"{b} = {g} * {f}")
