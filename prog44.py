# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:42:28 2020

@author: Pawan
"""
'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains N. The second line contains an array of N integers each separated by a space.
5
1 2 3 4 5 5 6'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])
