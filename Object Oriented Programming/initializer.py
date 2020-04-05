#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 04:08:51 2020

@author: eneskuralay
"""

class Animal(object):
    
    def __init__(self,a,b):    # a = name , b = age
        self.name = a
        self.age = b
        
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
a1 = Animal("dog",2)
a2 = Animal("cat",3)
a3 = Animal("bird",1)

print(a1.getAge())
print(a2.getName())
print(a3.getName(),a3.getAge())