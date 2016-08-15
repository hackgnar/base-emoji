#!/usr/bin/python
# -*- coding: utf-8 -*- 
exec("a=[]\ndef dont_fail(x,l):\n\ttry:\n\t\tl.append(hex(x)[2:].decode('hex').decode('utf-8'))\n\texcept:\n\t\tpass\n")
e=[(u'😀',u'🙏'),(u'☂',u'➰'),(u'🚀',u'🛀'),(u'🌀',u'🗿')]
x = lambda x,y:int(x[y].encode('utf-8').encode('hex'), 16)
[[ dont_fail(j,a) for j in range(x(s,0)-1,x(s,1) )] for s in e]
b = dict((i, j[0] + j[1]) for i,j in enumerate(__import__("itertools").combinations(a,2)) if i < 65536)

def emoji_encode(s):
    result = ""
    data = s.encode('hex')
    for i in range(0, len(data), 4):
        result += b[int(data[i:i+4],16)]
    return result

def emoji_decode(s):
    c = dict((v,k) for k,v in b.iteritems()) 
    d = '\xf0'
    data =  [d+i for i in s.encode('utf-8').split(d) if i != ""]
    tmp = []
    for j in data:
        d = '\xe2'
        if d in j:
            tmp += [k if k.startswith('\xf0') else d+k for k in j.split(d)]
        else:
            tmp.append(j)
    data = tmp
    result = ''
    for i in range(0, len(data), 2):
        try:
            foo = hex(c[(data[i] + data[i+1]).decode('utf-8')])[2:].zfill(4)
            #result += hex(c[(data[i] + data[i+1]).decode('utf-8')])[2:]
            result += foo
        except:
            print 'fail'
    return result.decode('hex')

#following is for testing...
import sys
data = sys.stdin.read()
foo = emoji_encode(data)
print foo
bar = emoji_decode(foo)
print bar
