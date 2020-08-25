# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:55:34 2020

@author: Pawan
"""
'''
You are given a positive integer N . Print a numerical triangle of height N-1 like the one below:
1
22
333
4444
55555
......'''

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i)//9*i)