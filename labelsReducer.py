#!/usr/bin/python

import sys

def calculateLabels():
  # input comes from STDIN
  for line in sys.stdin:
    index, a, b, c, d, e, f, g = line.split(',')
    print(index)

if __name__ == "__main__":
  calculateLabels()
