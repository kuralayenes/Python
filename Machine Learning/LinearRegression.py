#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:46:54 2020

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

# prediction
import numpy as np

b0 = linear_reg.predict([[0]])
print("b0: ",b0)    # y eksenini kestiği nokta intercept

b0_ = linear_reg.intercept_ # y eksenini kestiği nokta intercept
print("b0_: ",b0_)

b1 = linear_reg.coef_ # eğim slope
print("b1: ", b1)

# maas tahmin (predict) y =  b0 + b1 * x

maas_yeni = b0 + b1 * 11
print("11 yıllık deneyimli maaş: ",maas_yeni)

print(linear_reg.predict([[11]]))


array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1)

plt.scatter(x,y)
plt.show()

y_head = linear_reg.predict(array)
plt.plot(array, y_head, color= "blue")
 














