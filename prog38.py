# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:42:54 2020

@author: Pawan
"""
'''You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''

def wrap(string, max_width):
    y=max_width
    z=0
    return_string = ""
    for i in range(0,len(string),y):
        return_string += string[0+z:y+z] + "\n"  
        z+=max_width
    return return_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
