#-*- coding: utf-8 -*-
import urllib2

request = urllib2.Request("http://python.jobbole.com/81336/")
response = urllib2.urlopen(request)
with open('./a.txt','w') as fp:
	fp.write(response.read())
print('获取url信息，response.geturl():%s'%response.geturl())
print('获取返回代码，response.getcode():%s'%response.getcode())
print('获取返回信息，response.info():%s'%response.info())
