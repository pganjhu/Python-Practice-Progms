# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:36:21 2020

@author: Pawan
"""
'''
The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
count = list(map(int,input().strip().split()))
m = count[0]
n = count[1]
Arr = list(map(int,input().strip().split()))
array = set(map(int,input().strip().split()))
array2 = set(map(int,input().strip().split()))
points = 0
for i in Arr:
    if i in array : 
        points = points + 1
    elif i in array2 : 
        points = points - 1
print (points)
