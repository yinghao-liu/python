#!/usr/bin/env python3
def printf(*arg):
	for val in arg:
		print(val)

if "__main__" == __name__:
	printf(1,2,3,4)
