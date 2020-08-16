# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:44:51 2020

@author: Pawan
"""

'''Define a function which can print a dictionary where the keys are numbers between 
1 to n (both included) and the values are square of keys.'''

def squareddict(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    print(d) #prints key value pair
    for k in d.keys():
        print (k) #prints only keys
    for (k,v) in d.items(): #prints values not keys
        print (v)
    
squareddict(8)