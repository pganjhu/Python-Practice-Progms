# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:39:57 2020

@author: Pawan
"""
'''
You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
string=input()
s=list(string)
uc=[]
lc=[]
evendigit=[]
odddigit=[]
for i in range(len(s)):
    if s[i].isdigit():
        if int(s[i])%2==0:
            evendigit.append(s[i])
        if int(s[i])%2==1:
            odddigit.append(s[i])
    if s[i].isalpha():
        if s[i].isupper():
            uc.append(s[i])
        if s[i].islower():
            lc.append(s[i])
uc.sort()
lc.sort()
evendigit.sort()
odddigit.sort()
x=lc+uc+odddigit+evendigit
print(''.join(str(i) for i in x))