# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:59:55 2020

@author: Pawan
"""

"""
Let's dive into decorators! You are given  mobile numbers. Sort them in ascending order then print them in the standard format shown below:


+91 xxxxx xxxxx

The given mobile numbers may have ,  or  written before the actual  digit number. Alternatively, there may not be any prefix at all.

Input Format

The first line of input contains an integer , the number of mobile phone numbers.
 lines follow each containing a mobile number.

Output Format

Print  mobile numbers on separate lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878
Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230"""
def wrapper(f):
    def phone(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return phone
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


