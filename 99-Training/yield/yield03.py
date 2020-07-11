#!/usr/bin/env python
# -*- coding: utf-8 -*-

def go():
	


def subtask():
    i = -1 
    while True:
        a = yield i
        i += 1
        print "--- come from parent ", a

if __name__ == '__main__':
	c = subtask()

	i_first = c.next() # 启动协程,之后下面就可以send通信了
	print "from subtask first", i_first

	for i in range(10):
	    sub = c.send(i)
	    print "come from subtask ", sub