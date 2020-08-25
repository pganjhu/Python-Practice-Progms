# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:24:59 2020

@author: Pawan
"""
'''
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.'''
def count_substring(string, sub_string):
    results = 0
    sub_len = len(sub_string)
    for i in range(len(string)):
        if string[i:i+sub_len] == sub_string:
            results += 1
    return results

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

