#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 03:28:06 2020

@author: eneskuralay
"""

class Emp(object):
    age = 25
    salary = 1000       # $
    
    def ageSalaryRatio(self):
        result = self.age / self.salary
        print("Method: ",result)
        return result


def ageSalaryRatio(age,salary):
    result = age/salary
    print("Func: ",result)
    return result


e1 = Emp()
e1.ageSalaryRatio()
print(e1.ageSalaryRatio())

age1= 30
salary1 = 3000

ageSalaryRatio(age1,salary1)
print(ageSalaryRatio(age1,salary1))

## Area

def findArea(a,b):      # a = pi , b = r
    
    area = a*b**2
    return area

pi = 3.14
r = 5

result1 = findArea(pi,r)
result2 = findArea(pi,10)

result3 = result1 + result2

print("result 1 : ",result1," result 2 : ",result2," result 3 : ",result3)


       