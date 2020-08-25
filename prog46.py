# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:26:36 2020

@author: Pawan
"""
'''Problem statement
Print all possible palindromic partitions in the given string. Please don’t consider the string case.
Example
Input: BorrowOrRob
Output:
1. B o r r o w O r R o b
2. BorrowOrRob
3. B orro w OrRo b
4. B o rr o w OrRo b
5. B orro w O rR o b
6. B o rr o w O rR o b'''

#A recursive function to partition the string
def partition_fun(string,itr, res,temp):
    temp_str=''
    current = temp[:]
    for i in range(itr, len(string)):
        temp_str=temp_str+string[i]
        if palindrome(temp_str): #call to function palindrome line 34
            temp.append(temp_str)
            if i+1<len(string):
                partition_fun(string, i+1, res,  temp[:]) #recursive call
            else:
                res.append(temp)
            temp=current

#A function to check palindrome
def palindrome(str):
    str_rev=str[:][::-1]
    if str==str_rev:
        return True
    else:
        return False

#Main  call to functions
if __name__ == "__main__":
    string = str(input("Please enter the string : ").strip())
    string=string.lower() #convert the given string to lower case
    length=len(string)
    res = []
    partition_fun(string, 0, res,[])
    c=1
    for i in res:
        word = ''.join(i)
        if len(word)==length:
            print(c," : ",*i, sep=' ')
        c=c+1