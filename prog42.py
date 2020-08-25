# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:29:49 2020

@author: Pawan
"""
'''
Python question by HackerRank
TODO 1:
Consider the following:
A string, , of length N where S=co, c1, ... cn-1.
An integer, k, where k is a factor of n.
We can split S into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in S. Then, use each ti to create string ui such that:
The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string .
Given S and k, print n/k lines where each line i denotes string ui.
Input Format
The first line contains a single string denoting S.
The second line contains an integer, k, denoting the length of each subsegment.
Constraints: 1<= n <= 10**4,  , where n is the length of S
1 <= k <= n,
It is guaranteed that n is a multiple of k.
Output Format: Print n/k lines where each line i contains string ui.
'''
def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        line = string[i:i+k]
        seen = set()
        for i in line:
            if i not in seen:
                print(i,end="")
                seen.add(i)
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)