#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:42:24 2020

@author: eneskuralay
"""



# Parent

class Animal(object):
    def __init__(self):
        print("Animal is created")
        
    def toString(self):
        print("animal")
    
    def walk(self):
        print("animal walk")
    
# Child
        
class Monkey(Animal):
    
    def __init__(self):
        super().__init__()          # use init of parent (animal) class
        print("Monkey is created")
        
    def toString(self):
        print("Monkey")
    
    def climb(self):
        print("Monkey can climb")
        

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("Bird is created")
    
    def fly(self):
        print("fly")


m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()

print("-"*20)

b1 = Bird()
b1.walk()
b1.fly()

