#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
  def __init__(self, name):
    self.name = name

if __name__ == '__main__':
  a = Student('qianm')
  print(a.name)
