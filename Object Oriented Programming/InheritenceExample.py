#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:15:14 2020

@author: eneskuralay
"""

class Website(object):

    "parent"
    
    def __init__(self,name,surname):
        
        self.name = name
        self.surname = surname
        
    def loginInfo(self):
        print(self.name + " " + self.surname)
        
       


class Website1(Website):
    
    "child"
    
    def __init__(self, name, surname, ids):
        
        Website.__init__(self, name, surname) #super() or parent name
        self.ids = ids
        
    def login(self):
        
        print(self.name + " " + self.surname + " " + self.ids )
        



class Website2(Website):
    
    "child"
    
    def __init__ (self, name, surname, email):
        
        Website.__init__ (self,name,surname)
        self.email = email
    
    def login(self):
        
        print(self.name + " " + self.surname + " " + self.email ) 
        
       
        
        
p1 = Website("enes","kuralay")
p1.loginInfo() 

print("-"*20)

p2 = Website1("enes","kuralay","123")
p2.login()

print("-"*20)

p3 = Website2("enes","kuralay","email@-- .com")
p3.login()














        