#!/usr/bin/env python3

class a:
    def show( message):
        print("this is class a, message is {}, normal".format(message))

class b:
    @classmethod
    def show(cls, message):
        print("this is class b, message is {}, classmethod".format(message))

class c:
    @staticmethod
    def show(message):
        print("this is class c, message is {}, staticmethod".format(message))
if "__main__" == __name__:
    print(a.show)
    print(b.show)
    print(c.show)
    a.show(1)
    b.show(2)
    c.show(3)
    ins1=a()
    ins2=b()
    ins3=c()
    ins2.show(20)
    ins3.show(30)
    ins1.show(10)
