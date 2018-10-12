#!/usr/bin/env python3

class dog:
    data="this is dog data"
    def init(self, name):
        self.kind=name


if "__main__" == __name__:
    a=dog()
    b=dog()
    print(dog.init)
    print(a.init)
    a.init("wang")
    b.init("miao")
    print(a.kind)
    print(b.kind)

    a.kk=123
    b.kk=234
    print(a.kk)
    print(b.kk)

