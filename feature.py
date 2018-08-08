#!/usr/bin/env python3

class name:
	"""doccccccccc"""
	def __init__(self):
		self.va="va"	# instance variable unique to each instance
		self.va_mutable=["va"]
	def print_name(self):
		print("hello there")

	"""second doccc"""
	__aa="pseudo private aa"
	bb="public immutable bb" # class variable shared by all instances in initial, see the differences between mutable and immutable variables 
	__aa_mutable=["aa_mutable"]
	bb_mutable=["bb_mutable"]


if "__main__" == __name__:
	obj1=name();
	obj1.print_name()
	print(obj1.__doc__)
	print(obj1.va)
	print(obj1.va_mutable)
	#this is called name mangling, it still is possible to access or modify a variable that is considered private.
	print(obj1._name__aa)
	print(obj1._name__aa_mutable)
	print(obj1.bb)
	print(obj1.bb_mutable)

	print("----------------------")
	obj2=name();
	obj1.va="va after modify"
	obj1.va_mutable.append("va_mutable after modify")
	obj1._name__aa="private aa, after modify"
	obj1._name__aa_mutable.append("aa_mutable after modify")
	obj1.bb="class variable bb after modify"
	obj1.bb_mutable.append("bb_mutable after modify")
	print(obj1.va)
	print(obj1.va_mutable)
	print(obj1._name__aa)
	print(obj1._name__aa_mutable)
	print(obj1.bb)
	print(obj1.bb_mutable)
	print("+++++++++++++++++++++")
	print(obj2.va)
	print(obj2.va_mutable)
	print(obj2._name__aa)
	print(obj2._name__aa_mutable)
	print(obj2.bb)
	print(obj2.bb_mutable)
