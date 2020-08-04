# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:33:42 2020

@author: Pawan
"""
'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
values=input('enter list of numbers: ')
l=values.split(",")
t=tuple(l)
print (l)
print (t)