#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 05:02:32 2020

@author: eneskuralay
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("decision_tree.csv", sep=";", header= None)

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)


#%% decision tree

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()

tree_reg.fit(x,y)

tree_reg.predict([[6.2]])

x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = tree_reg.predict(x_)


#%% visualize

plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color="blue")

plt.xlabel("Match Level")
plt.ylabel("Price")
plt.show()




