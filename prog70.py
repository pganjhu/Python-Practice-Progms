# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:14:10 2020

@author: Pawan
"""
'''
Task
You are given the coefficients of a polynomial P. 
Your task is to find the value of P at point x.
Input Format
The first line contains the space separated value of the coefficients in P. 
The second line contains the value of x.
Output Format
Print the desired value.
Sample Input
1.1 2 3
0
Sample Output
3.0
'''
import numpy as np
n = list(map(float,input().split()))
m = input()
print(np.polyval(n,int(m)))

