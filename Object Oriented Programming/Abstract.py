#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:19:58 2020

@author: eneskuralay
"""

from abc import ABC, abstractmethod

class Animal(ABC):          # Super class 
    
    @abstractmethod
    def walk(self): pass

    
    def run(self): pass

class Bird(Animal):         # Sub class
    
    def __init__(self):
        print("bird")
    
    def walk(self):
        print("walk")

b1 = Bird()
        
    