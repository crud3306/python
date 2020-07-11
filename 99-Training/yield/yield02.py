#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fun():
	for i in range(20):
		x=yield i
		print('good',x)

if __name__ == '__main__':
	a=fun()
	print(a)
	x = a.next()
	print(x)
	x=a.send(5)
	print(x)