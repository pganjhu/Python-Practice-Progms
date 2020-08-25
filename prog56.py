# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:11:44 2020

@author: Pawan
"""
'''
Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
actions = {
    "append":d.append, 
    "appendleft": d.appendleft,
    "pop": d.pop,
    "popleft": d.popleft
}
for i in range(int(input())):
    action = input().split()
    if len(action)>1:
        x,y = action
        actions[x](int(y))
    else:
        actions[action[0]]()
print(*d)
