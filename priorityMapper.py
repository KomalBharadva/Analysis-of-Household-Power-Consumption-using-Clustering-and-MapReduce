#!/usr/bin/python

import sys
import random

def passDataToCalculateInitialCentroids():
  for eachRow in sys.stdin:
    print(str(eachRow.strip().split(","))+";"+str(random.uniform(0,1)))

if __name__ == "__main__":
  passDataToCalculateInitialCentroids()
