# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:00:06 2020

@author: Pawan
"""
'''Python has built-in string validation methods for basic data. 
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.'''
if __name__ == '__main__':
    s=input()
    print (any(c.isalnum() for c in s))
    print (any(c.isalpha() for c in s))
    print (any(c.isdigit() for c in s))
    print (any(c.islower() for c in s))
    print (any(c.isupper() for c in s))

