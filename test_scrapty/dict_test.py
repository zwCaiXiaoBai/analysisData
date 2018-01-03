#!/usr/bin/env python

'''
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for tup in s:
    print('name: %s' % tup[0])
    print('age: %d' % tup[1])
'''
import sys

d = {'adam': 20, 'lisa': 85, 'bart': 59}
for vals in d:
    print(vals)

'''
t = 'a','b'
print(t[0])
'''

'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

'''

L = ['adma','lisa','bart','paul']
print(L[-4:-1:2])


print (__name__)


print('sys.path: %s'% sys.path)

print('a'+'b')