#!/usr/bin/python
listt = [1,2,3,4,5,6]
it = iter(listt)
print(next(it))
print(next(it))
print("here is for")
for x in it:
	print(x)

def fab(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n = n+1
f = fab(4)

print("yield")
print(next(f))
print(next(f))
print(next(f))
print(next(f))
