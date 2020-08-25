# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:51:57 2020

@author: Pawan
"""
'''
The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]'''

if __name__ == '__main__':
    N = int(input())
    m=list()
    for i in range(N):
       method,*l=input().split()
       k=list(map(int,l))
       if len(k)==2:
          q=[k[0]]
          w=[k[1]]
       elif len(k)==1:
          q=[k[0]]
       if method =='insert':
          m.insert(q[0],w[0])
       elif method == 'append':
          m.append(q[0])
       elif  method == 'remove':
          m.remove(q[0])
       elif method =='print':
          print(m)
       elif method == 'reverse':
          m.reverse()
       elif method =='pop':
          m.pop()
       elif method == 'sort':
          m.sort()
