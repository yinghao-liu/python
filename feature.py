#!/usr/bin/env python3

#with only do the finally suite, we still need try before with
# refer to https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
#refer to https://www.cnblogs.com/huclouy/p/6115829.html
try:
	with open("aa") as fd:
		print("open OK")
except FileNotFoundError as a:
	print(a.strerror)
except:
	print("all other exception")
else:
	print("if no exception")
finally:
	print("alway")
	
