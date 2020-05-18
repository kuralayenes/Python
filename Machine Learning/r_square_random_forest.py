#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 06:34:33 2020

@author: eneskuralay
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("decision_tree.csv",sep=";", header= None)


x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

#%%

from sklearn.ensemble import RandomForestRegressor

rand_forest = RandomForestRegressor(n_estimators = 100, random_state = 42)


rand_forest.fit(x,y)


y_head = rand_forest.predict(x)

#%%

from sklearn.metrics import r2_score

print("r_score", r2_score(y,y_head))

















