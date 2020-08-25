# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:57:57 2020

@author: Pawan
"""

'''Define a class named American which has a static method called printNationality.
Use @staticmethod decorator to define class static method.'''

class American(object):
    @staticmethod
    def printNationality():
        print ("America")

am = American()
am.printNationality()
American.printNationality()