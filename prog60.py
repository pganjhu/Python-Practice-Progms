# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:33:10 2020

@author: Pawan
"""
'''
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = input()
m = input().split()
N = input()
n = input().split()
print ("\n".join(sorted(list(set(m) ^ set(n)),key=int)))
