# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:42:37 2020

@author: Pawan
"""

'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,...,Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''
import numpy
w, h = int(input("enter no. of rows")),int(input("enter no. of columns"))
Matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        Matrix[j][i]=i*j
print(numpy.transpose(Matrix))