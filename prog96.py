# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 02:10:41 2020

@author: Pawan
"""
"""In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions."""
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input()
s=''
for i in range(0,len(a)):
    if i!=0:
        if a[i]==a[i-1]:  
            continue
    p=0
    for j in range(i,len(a)):
        if a[i]==a[j]:
            p+=1
        else:
            break
    s+='('+str(p)+', '+a[i]+')'+' '
print(s)
