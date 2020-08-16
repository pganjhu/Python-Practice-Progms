# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:56:32 2020

@author: Pawan
"""
def gen(mystr):
    for i in mystr:
        yield i
def text(mytext):
    for i in mytext:
        yield i*2
mystr="abcde"
print("".join(text(gen(mystr))))

def ext():
    global q
    q=40
    def intf():
        global q
        q=60
        print('q=',q)
    q=20
ext()
print(q)

from functools import reduce
def process(nos):
    ans=reduce(lambda x,y:x if x else y, nos)
    return ans
if __name__=='__main__':
    try:
        mynos=[3,34,26,11,19,72,12,25,10,66]
        output=process(mynos)
        print(output)
    except TypeError:
        print("erroe")
        
        
mylist=['Python','is','a','programming','language']
b=[]
try:
    for i in mylist:
        if 'n' in i:
            b.extend(i.split('n'))
except IndexError:
    print("List Index")
print(b)

import threading
def thread1():
    print("first")
def thread2():
    print("second")
t1=threading.Thread(target=thread1)
t2=threading.Thread(target=thread2)
t1.start()
print("abc :{}",format(threading.main_thread().name))

def sum(list):
    if len(list)==1:
        if list[0]%2:
            return list[0]
        else:
            return 0
    else:
        if list[0]%2:
            return list[0]+sum(list[1:])
        else:
            return sum(list[1:])
print(sum([5,7,3,8,5,6]))

import re
mystr="Hello World, This is Python Programming"
print(re.findall(r'P.+n ',mystr))
print(re.findall(r'P[a-z]*n',mystr))