#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:33:05 2020

@author: eneskuralay
"""



class Animal(object): # PARENT
    
    def toString(self):
        print("Animal")

class Monkey(Animal):  # CHİLD
    
    def toString(self):
        print("Monkey")
        
a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString()
    
    