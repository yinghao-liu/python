#!/usr/bin/env python3

class a:
    me="class a"

class b(a):
    pass

class c():
    me="class c"

class d(b, c):
    pass

if "__main__" == __name__:
    ins=d()
    print(ins.me) # output "class a"
