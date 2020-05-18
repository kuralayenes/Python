#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 06:47:47 2020

@author: eneskuralay
"""

# import library
import pandas as pd
import matplotlib.pyplot as plt

# import data
df = pd.read_csv("original.csv", sep=";")

# plot data
plt.scatter(df.deneyim, df.maas)
xlabel = "Deneyim"
ylabel = "Maas"
plt.show()
#%%
# Linear Regression

# Sklearn library
from sklearn.linear_model import LinearRegression

# linear regression model
linear_reg = LinearRegression()

x = df.deneyim.values.reshape(-1,1)
y = df.maas.values.reshape(-1,1)

linear_reg.fit(x,y)

y_head = linear_reg.predict(x)
plt.plot(x, y_head, color= "red")
 
#%%

from sklearn.metrics import r2_score

print("r square score: ",r2_score(y,y_head))












