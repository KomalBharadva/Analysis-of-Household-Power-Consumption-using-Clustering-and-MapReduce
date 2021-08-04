#!/usr/bin/python

import sys

def calculateNewCentroids():
  global centroid_index
  current_centroid = None
  sum_a = 0
  sum_b = 0
  sum_c = 0
  sum_d = 0
  sum_e = 0
  sum_f = 0
  sum_g = 0
  count = 0
  # input comes from STDIN
  for line in sys.stdin:
    # Get (Centroid Index) and (Features)
    centroid_index, a, b, c, d, e, f, g = line.split('\t')
    # Floating the features
    try:
      a = float(a)
      b = float(b)
      c = float(c)
      d = float(d)
      e = float(e)
      f = float(f)
      g = float(g)
    except ValueError:
      continue
    if current_centroid == centroid_index:
      count += 1
      sum_a += a
      sum_b += b
      sum_c += c
      sum_d += d
      sum_e += e
      sum_f += f
      sum_g += g
    else:
      if count != 0:
        print(str(current_centroid) + ", " + str(sum_a) + ", " + str(sum_b) + ", " + str(sum_c) + ", " + str(sum_d) + ", " + str(sum_e) + ", " + str(sum_f) + ", " + str(sum_g) + ", " + str(count))
      current_centroid = centroid_index
      sum_a = a
      sum_b = b
      sum_c = c
      sum_d = d
      sum_e = e
      sum_f = f
      sum_g = g
      count = 1
  # Cluster
  if current_centroid == centroid_index and count != 0:
    print(str(current_centroid) + ", " + str(sum_a) + ", " + str(sum_b) + ", " + str(sum_c) + ", " + str(sum_d) + ", " + str(sum_e) + ", " + str(sum_f) + ", " + str(sum_g) + ", " + str(count))

if __name__ == "__main__":
  calculateNewCentroids()
