#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:11:52 2020

@author: eneskuralay
"""

class Calc(object):
    
    def __init__(self,a,b):
        
        self.value1 = a
        self.value2 = b
        
    def Add(self):
        return self.value1 + self.value2
    
    def Multiply(self):
        return self.value1 * self.value2
    
    def Division(self):
        return self.value1 / self.value2

    def Minus(self):
        return self.value1 - self.value2
    
print("Selection 1- Add , 2- Multiply , 3- Division , 4- Minus")
select = input("Select 1-2-3-4 :  ")

v1 = int(input("v1 Value : "))
v2 = int(input("v2 Value : "))

c1 = Calc(v1,v2)

if select == "1":
    add_result = c1.Add()
    print("v1 + v2 = {} ".format(add_result))
    
elif select == "2":
    multiply_result = c1.Multiply()
    print("v1 * v2 = {} ".format(multiply_result))

elif select == "3":
    division_result = c1.Division()
    print("v1 / v2 = {} ".format(division_result))

elif select == "4":
    minus_sonuc = c1.Minus()
    print("v1 - v2 = {} ".format(minus_sonuc))

else:
    print("404 Not Found !!")    



















