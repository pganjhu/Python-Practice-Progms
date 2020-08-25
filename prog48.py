# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:43:07 2020

@author: Pawan
"""
'''The calendar module allows you to output calendars and provides additional useful functions for them.
class calendar.TextCalendar([firstweekday])
This class can be used to generate plain text calendars.
Task
You are given a date. Your task is to find what the day is on that date.
Input Format
A single line of input containing the space separated month, day and year, respectively, in    format.
Constraints
Output Format
Output the correct day in capital letters.
Sample Input
08 05 2015
Sample Output
WEDNESDAY'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

day = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}

m,d,y = map(int,input().split())
print (day[calendar.weekday(y,m,d)])