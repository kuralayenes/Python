#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:46:05 2020

@author: eneskuralay
"""

class Employee(object):
    
    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print("Employee : ",result)
class compEng(Employee):
    
    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print("CompEng : ", result)
class EEE(Employee):
    
    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * raise_rate   
        print("EEE : ",result)
    
e1 = Employee()

c1 = compEng()

eee1 = EEE()


employee_list = [c1,eee1]

for employee in employee_list:
    employee.raisee()
    