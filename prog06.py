# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:39:33 2020

@author: Pawan
"""
'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
'''
import math
C=50
H=30
D=int(input("Enter the values :"))
print(math.sqrt((2*C*D)/H))