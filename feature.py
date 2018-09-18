#!/usr/bin/env python3.7
import subprocess

if "__main__" == __name__:
	subprocess.run("ps -ef |  grep init | grep -v grep".split(), shell=True)
	ret=subprocess.run("ping -c2 baidu.com".split(), timeout=3, capture_output=True)
	print(ret)
	try:
		subprocess.run("ping baidu.com".split(), timeout=3)
	except subprocess.TimeoutExpired as a:
		print("process should been killed".format(a))
	try:
		"""
		when shell is True, timeout can not kill the program(ping, below), it can only kill its parent process(the shell)
		refer to https://stackoverflow.com/questions/48763362/python-subprocess-kill-with-timeout
		"""
		subprocess.run("ping baidu.com", shell=True, timeout=3)
	except subprocess.TimeoutExpired as b:
		print("------{}-------".format(b))

	


