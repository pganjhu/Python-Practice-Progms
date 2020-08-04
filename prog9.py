# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:59:30 2020

@author: Pawan
"""

'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
lines = []
while True:
    s = input("Start entering lines")
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print (sentence)