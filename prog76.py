# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:00:11 2020

@author: Pawan
"""

"""
Problem Statement
dot
The dot tool returns the dot product of two arrays.
import numpy
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print numpy.dot(A, B)       #Output : 11
cross
The cross tool returns the cross product of two arrays.
import numpy
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print numpy.cross(A, B)     #Output : -2
Task
You are given two arrays A and B. Both have dimensions of NXN. 
Your task is to compute their matrix product.
Input Format
The first line contains the integer N. 
The next N lines contains N space separated integers of array A. 
The following N lines contains N space separated integers of array B.
Output Format
Print the matrix multiplication of A and B.
Sample Input
2
1 2
3 4
1 2
3 4
Sample Output
[[ 7 10]
 [15 22]]
 """
from __future__ import print_function
import numpy
n=int(input())
a = numpy.array([input().split() for _ in range(n)],int)
b = numpy.array([input().split() for _ in range(n)],int)
m = numpy.dot(a,b)
print (m)