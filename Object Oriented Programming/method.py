#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 03:12:14 2020

@author: eneskuralay
"""

class Square: # Or class Square(object):
    
    edge = 5    #meter
    area= 0
    
    def Area(self):
        self.area = self.edge * self.edge 
        print("Area: ",self.area)
        
        
s1 = Square()

print(s1.edge)

s1.Area()

s1.edge = 7
s1.Area()


    