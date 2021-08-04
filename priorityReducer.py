#!/usr/bin/python

import sys

size = 4
centDict = dict()
def calculateCentroids():
  for eachLine in sys.stdin:
    givenKey, tempPriorityValue = eachLine.split(";")
    priorityValue = float(tempPriorityValue)
    if len(centDict) < size:
      centDict[priorityValue] = givenKey
    else:
      if min(centDict.keys()) < priorityValue:
        del centDict[min(centDict.keys())]
        centDict[priorityValue] = givenKey
  tempList = list(centDict.values())
  for eachValue in tempList:
    tempArray = eachValue.strip().split(",")
    arrayLength = len(tempArray)
    lastItem = arrayLength - 1
    tempArray[0] = tempArray[0][1:]
    tempArray[lastItem] = tempArray[lastItem][0:len(tempArray[lastItem])-1]
    for i in range(0, arrayLength):
      tempArray[i] = tempArray[i].replace(" ","")
      tempArray[i] = tempArray[i].replace("'","")
      tempString = ""
      for i in range(0, arrayLength):
        if(i != lastItem):
          tempString = tempString + tempArray[i] + ", "
        else:
          tempString = tempString + tempArray[i]
    print(tempString)

if __name__ == "__main__":
  calculateCentroids()
