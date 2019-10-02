#!/usr/bin/env python3

### decorator
print("------ decorator ------")
def ff(fc):
	print("in ff and arg is {}".format(fc))
	fc()
	return ff
@ff
def func_decor():
	print("in function func_decor")
print("---------------")
func_decor()


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


