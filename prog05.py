# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:36:49 2020

@author: Pawan
"""
'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string :")

    def printString(self):
        print (self.s.upper())

obj=InputOutString()
obj.getString()
obj.printString()