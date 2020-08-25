# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:53:55 2020

@author: Pawan
"""
'''-7


2
Given the names and grades for each student in a Physics class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input:

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Output:

>>Berry
>>Harry'''
if __name__ == '__main__':
    n=int(input())
    names=[]
    scores=[]
    for i in range(n):
        name=input()
        names.append(name)
        score=float(input())
        scores.append(score)
    dic=dict(sorted(zip(names,scores)))
    mini=(min(scores))
    cnt=scores.count(mini)
    for i in range(cnt):
        scores.remove(mini)
    minim=min(scores)
    for i,j in dic.items():
        if j==minim:
            print(i)
