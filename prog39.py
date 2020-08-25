# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:45:36 2020

@author: Pawan
"""
'''Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
lstr = '.|.'
varbl=input().split()
midString = 'WELCOME'
breakpt = (int(varbl[0])-2)//2

for i in range(int(varbl[0])):

    print((lstr*((2*i)+1)).center(int(varbl[1]),'-'))
    if i == breakpt:
        print(midString.center(int(varbl[1]),'-'))
        break 
       
i = int(varbl[0])//2          
while i > 0:
    pattern = lstr * ((2 * i) - 1) 
    print (pattern.center (int(varbl[1]), '-')) 
    i = i-1
