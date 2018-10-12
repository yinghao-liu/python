#!/usr/bin/env python3

value=100
def scope_test():
    value=10 # this is for 'nonlocal' in do_nonlocal
    def do_local():
        value=1
        print("this is in do local, value is {}".format(value))

    def do_nonlocal():
        nonlocal value # The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals.
        value+=1
        print("this is in do_nonlocal value is {}".format(value))

    def do_global():
        global value
        value+=1
        print("this is in do_global, value is {}".format(value))
    do_local()
    do_nonlocal()
    do_global()

if "__main__" == __name__:
    scope_test()
    print("this is in main, value is {}".format(value))


