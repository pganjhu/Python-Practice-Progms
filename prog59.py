# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:24:24 2020

@author: Pawan
"""
'''
Now, lets use our knowledge of Sets and help 'Mickey'.
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student 'Mickey' to compute an average of all the plants with distinct heights in her greenhouse.
Formula used:
Average=SumofDistinctHeightsTotalNumberofDistinctHeights
Input Format
First line contains, total number of plants in greenhouse.
Second line contains, space separated height of plants in the greenhouse.
Total number of plants is upto 100 plants.
Output Format
Output the average value of height.
Sample Input
10
161 182 161 154 176 170 167 171 170 174
Sample Output
169.375'''

from __future__ import division
def average(array):
    # your code goes here
    s1=(set(arr))
    p= (sum(s1)/len(s1))
    return (p)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
