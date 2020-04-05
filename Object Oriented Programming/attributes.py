#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:43:24 2020

@author: eneskuralay
"""


class Footballer(object):
    
    football_club = "Barcelona"
    age = 30
    
f1 = Footballer()

print(f1)
print(f1.football_club)
print(f1.age)


f1.football_club = "Real Madrid"
print(f1.football_club)

