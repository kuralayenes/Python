#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:22:39 2020

@author: eneskuralay
"""

class BankAccount(object):
    
    def __init__(self,name,money,address):
        self.name = name
        self.__money = money
        self.address = address
    
    # get and set Global 
    
    def getMoney(self):
        return self.__money
    
    def setMoney(self,amount):
        self.__money = amount
    
    # Private
    
    def __increase(self):
        self.__money = self.__money + 500
        
p1 = BankAccount("Messi",1000,"Barcelena")
p2 = BankAccount("Neymar",750,"Paris")

print("get Method: ", p1.getMoney())

p1.setMoney(5000)
print("after set Method: ", p1.getMoney())
 
#p1.__increase()
#print("after Raise ",p1.getMoney())
        
        
        
        
        