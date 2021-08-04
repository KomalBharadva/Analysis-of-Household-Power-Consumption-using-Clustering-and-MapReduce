#!/usr/bin/python

import sys
from math import sqrt

# This method is used to read centroid.txt file and return centroid values.
def getCentroids(filepath):
  centroids = []
  with open(filepath) as fp:
    line = fp.readline()
    while line:
      if line:
        try:
          line = line.strip()
          features = line.split(', ')
          centroids.append([float(features[0]), float(features[1]), float(features[2]), float(features[3]), float(features[4]), float(features[5]), float(features[6])])
        except:
          break
      else:
        break
      line = fp.readline()
  fp.close()
  return centroids

# This method is used to perform calculations and print values for reducer.
def createClusters(centroids):
  for eachLine in sys.stdin:
    features = eachLine.strip().split(',')
    min_dist = 1e8
    index = -1
    for centroid in centroids:
      try:
        features[0] = float(features[0])
        features[1] = float(features[1])
        features[2] = float(features[2])
        features[3] = float(features[3])
        features[4] = float(features[4])
        features[5] = float(features[5])
        features[6] = float(features[6])
      except ValueError:
        continue
      # Calculating euclidean distance from every point.
      cur_dist = sqrt(pow(features[0] - centroid[0], 2) + pow(features[1] - centroid[1], 2) + pow(features[2] - centroid[2],2) + pow(features[3] - centroid[3], 2) + pow(features[4] - centroid[4], 2) + pow(features[5] - centroid[5], 2) + pow(features[6] - centroid[6], 2))
      # Finding the centroid value that is closer to the point.
      if cur_dist <= min_dist:
        min_dist = cur_dist
        index = centroids.index(centroid)
    print("%s,%s,%s,%s,%s,%s,%s,%s" % (index, features[0], features[1], features[2], features[3], features[4], features[5], features[6]))

if __name__ == "__main__":
  centroids = getCentroids("centroids1.txt")
  createClusters(centroids)
