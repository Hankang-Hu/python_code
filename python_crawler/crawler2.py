import urllib2
import urllib
import cookielib

filename = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
postdata = urllib.urlencode({
	"username":"201524020425",
	"password":"020425"
	})
result = opener.open("http://ids.chd.edu.cn/authserver/login?service=http%3A%2F%2Fportal.chd.edu.cn%2F",postdata)
#cookie.save(ignore_discard=True,ignore_expires=True)
#result = opener.open("http://ids.chd.edu.cn/authserver/login?service=http%3A%2F%2Fportal.chd.edu.cn%2F")
#print result.read()
for item in cookie:
	print("username:"+item.name)
	print("password:"+item.value)