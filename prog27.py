# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:11:07 2020

@author: Pawan
"""

'''Define a class, which have a class parameter and have a same instance parameter.
Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later'''
    
class Person:
    name='person'
    def __init__(self,name=None):
        self.name=name
pawan=Person("Pawan")
print ("%s name is %s" % (Person.name, pawan.name))
kumar=Person()
kumar.name='Kumar'
print ("%s name is %s" % (Person.name, kumar.name))