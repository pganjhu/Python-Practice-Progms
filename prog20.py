# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:32:21 2020

@author: Pawan
"""

'''Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.'''

n = int(input())
divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
print(divBy7)

def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)
divChecker(n)