#!/usr/bin/python

import sys

def finalCalculation():
  current_index = None
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
    index, temp_sum_a, temp_sum_b, temp_sum_c, temp_sum_d, temp_sum_e, temp_sum_f, temp_sum_g, temp_count = line.split(',')
    try:
      temp_sum_a = float(temp_sum_a)
      temp_sum_b = float(temp_sum_b)
      temp_sum_c = float(temp_sum_c)
      temp_sum_d = float(temp_sum_d)
      temp_sum_e = float(temp_sum_e)
      temp_sum_f = float(temp_sum_f)
      temp_sum_g = float(temp_sum_g)
      temp_count = int(temp_count)
    except ValueError:
      continue
    if current_index == index:
      sum_a += temp_sum_a
      sum_b += temp_sum_b
      sum_c += temp_sum_c
      sum_d += temp_sum_d
      sum_e += temp_sum_e
      sum_f += temp_sum_f
      sum_g += temp_sum_g
      count += temp_count
    else:
      if count != 0:
        print(str(sum_a / count) + ", " + str(sum_b / count) + ", " + str(sum_c / count) + ", " + str(sum_d / count) + ", " + str(sum_e / count) + ", " + str(sum_f / count) + ", " + str(sum_g / count))
      current_index = index
      sum_a = temp_sum_a
      sum_b = temp_sum_b
      sum_c = temp_sum_c
      sum_d = temp_sum_d
      sum_e = temp_sum_e
      sum_f = temp_sum_f
      sum_g = temp_sum_g
      count = temp_count
  if count != 0:
    print(str(sum_a / count) + ", " + str(sum_b / count) + ", " + str(sum_c / count) + ", " + str(sum_d / count) + ", " + str(sum_e / count) + ", " + str(sum_f / count) + ", " + str(sum_g / count))

if __name__ == "__main__":
  finalCalculation()
