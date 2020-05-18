#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 06:05:13 2020

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

print("7.8 level : ",rand_forest.predict([[7.8]]))

x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)

y_head = rand_forest.predict(x_)

#%%

plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color="green")

plt.xlabel("Match Level")
plt.ylabel("Price")
plt.show()


















