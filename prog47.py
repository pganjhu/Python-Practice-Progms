# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:18:15 2020

@author: Pawan
"""
'''
We have a record of students. Each record contains the student's name, and their percent marks in Maths, 
Physics and Chemistry. The marks can be floating values. The user enters some integer 
followed by the names and marks for students. We are required to save the record in a dictionary data type. 
The user then enters a student's name. Output the average percentage marks obtained by that student, 
correct to two decimal places.'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_score=student_marks[query_name]
    a=(sum(query_score)/len(query_score))
    print("{0:.2f}".format(a))
            