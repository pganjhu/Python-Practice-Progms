# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:17:00 2020

@author: Pawan
"""
'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are 
divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:0100,0011,1010,1001
Then the output should be: 1010'''
value = []
items=[x for x in input("Enter : ").split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)
print (','.join(value))