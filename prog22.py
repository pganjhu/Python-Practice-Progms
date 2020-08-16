# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:40:13 2020

@author: Pawan
"""

'''Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line.'''

def fun_str(s1,s2):
    if len(s1)>len(s2):
        print(s1)
    elif len(s2)>len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)
s1=input("enter string 1: ")
s2=input("enter string 2: ")
fun_str(s1,s2)