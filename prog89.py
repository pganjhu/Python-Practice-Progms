# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:56:04 2020

@author: Pawan
"""

"""Neo has a complex matrix script. The matrix script is a  X  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

Capture.JPG

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers  (rows) and  (columns) respectively.
The next  lines contain the row elements of the matrix script.

Constraints


Note: A  score will be awarded for using 'if' conditions in your code.

Output Format

Print the decoded matrix script.

Sample Input 0

7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
Sample Output 0

This is Matrix#  %!"""
#!/bin/python3
import math
import os
import random
import re
import sys

x,y = list(map(int,input().split()))
rows =[input() for i in range(x)]
text = "".join([row[i] for i in range(y) for row in rows])
text = re.sub('([A-Za-z1-9])[^A-Za-z1-9]+([A-Za-z1-9])', r'\1 \2', text)
text = re.sub('  ', ' ', text)
print(text)