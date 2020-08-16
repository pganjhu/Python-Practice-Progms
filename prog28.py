# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:44:21 2020

@author: Pawan
"""

'''Define a function which can generate and print a tuple where the value are square of numbers between 1 and n (both included).'''
def SquareTuple(n):
    li=list()
    for i in range(1,n+1):
        li.append(i**2)
    print(li)
SquareTuple(20)

def SquareList(n):
    li=[]
    for i in range(1,n+1):
        li.append(i**2)
    print(li)
SquareList(20)

def SquareDict(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i**2
    print(d)
SquareDict(20)
        