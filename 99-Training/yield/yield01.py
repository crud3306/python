#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fun1():
	for i in range(20):
		x=yield i

if __name__ == '__main__':
	for x in fun1():
		print(x)