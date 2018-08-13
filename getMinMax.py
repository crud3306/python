#!/usr/bin/env python
# -*- coding: utf-8 -*-

def findMinAndMax(L):
  min = L[0]
  max = L[0]
  for x in L:
    if x<min:
      min = x
    if x>max:
      max=x
  return (min, max)

if __name__ == '__main__':
  print(findMinAndMax([1, -1, 9, 10, -3, 100]))
