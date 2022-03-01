#!/usr/bin/env python3

### decorator
print("------ decorator ------")
def decorator(fc):
    def wrapper(i):
        print("i is {}".format(i))
        print("in decorator-wrapper and arg is {}".format(fc))
        fc()
    print("in decorator")
    return wrapper

@decorator
def func():
	print("in function func")
print("---------------")
func("sss")


### parameter
print("\n------ parameter ------")
def func_param1(a, b, *c, **d):
	print(a)
	print(b)
	print(c)
	print(d)

func_param1(1,2,3,4, excess=1)

print("---------------")
def func_param2(a=1, b=2, *, c=4, **d):
	print(a)
	print(b)
	print(c)
	print(d)

func_param2(1,2,excess=1)

#func_param2(1,2,3,excess=1)
'''
def func_param3(a=1, b=2, *, **d):
	print(a)
	print(b)
	print(d)
	
func_param3()	
'''
### annotation
print("\n------ annotation ------")
def func_annot(a:print("parameter a"))->print("return annotation"):
	print("in func_annot : test annotation")
print("---------------")
func_annot(1)


