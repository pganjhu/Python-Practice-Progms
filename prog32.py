# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:04:39 2020

@author: Pawan
"""

'''Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area. 
Use def methodName(self) to define a method.'''

class Circle(object):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius * 2 * 3.14
ac=Circle(12)
print(ac.area())