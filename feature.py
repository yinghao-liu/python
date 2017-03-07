#!/usr/bin/python2.6
import urllib
f=urllib.urlopen("http://m.cnblogs.com/")
s=f.read()
print s
