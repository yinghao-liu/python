#!/usr/bin/env python3
import urllib.request
import urllib.error


url="http://www.asciima.com/logo.jpg"
head={}
#head["If-Modified-Since"]="Tue, 07 Jun 2016 01:27:43 GMT"
head["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
try:
	request=urllib.request.Request(url, headers=head)
	html=urllib.request.urlopen(request)
except urllib.error.HTTPError as err:
	print("err is {}, errno is {}, err reason is {}, headers is {}".format(err, err.code, err.reason, err.headers))

rst=html.read()
html.close()

fd = open("aa.jpg", "wb")
fd.write(rst)
fd.close()
