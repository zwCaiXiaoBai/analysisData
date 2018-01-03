# coding:utf8
from urllib.request import *
#import urllib.request.*
from envs.python35.Lib.http.cookiejar import CookieJar

url="http://www.baidu.com"

print  ('第一种方法')
response1 = urlopen(url)
print(response1.getcode())
print (len(response1.read()))


print("第二种方法")
request = Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urlopen(url)
print(response2.getcode())
print (len(response2.read()))

print("第三种方法")
cj = CookieJar()
opener = build_opener(HTTPCookieProcessor(cj))
install_opener(opener)
response3 = urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())
