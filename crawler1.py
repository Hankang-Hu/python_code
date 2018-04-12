import urllib2

request = urllib2.Request("http://python.jobbole.com/81336/")
response = urllib2.urlopen(request)
print response.read()