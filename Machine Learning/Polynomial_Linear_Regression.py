#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 01:53:08 2020

@author: eneskuralay
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("polynomial_linear_regression.csv", sep=";")

y = df.araba_max_hiz.values.reshape(-1,1)
x = df.araba_fiyat.values.reshape(-1,1)

plt.scatter(x,y)
plt.ylabel("Araba Max Hız")
plt.xlabel("Araba Fiyat")

# linear regression y = b0 + b1 * x
# Multiple regession y = b0 + b1 * x1 + b2 * x2 

# linear regression 
#%%
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x,y)


#%% predict

y_head = lr.predict(x)

plt.plot(x,y_head,color="red", label = "Linear")
plt.show

print(lr.predict([[10000]])) # not possible

#%% polynomial linear regression y = b0 + b1*x + b2*x^2 + ... +bn * x^n

from sklearn.preprocessing import PolynomialFeatures

polynomial_regression = PolynomialFeatures( degree = 2 ) # degree = n

x_poly = polynomial_regression.fit_transform(x)

#%% Fit
 
linear_Reg2 = LinearRegression()

linear_Reg2.fit(x_poly,y)

#%% Plot
y_head2 = linear_Reg2.predict(x_poly)
plt.plot(x,y_head2,color="green", label = "Poly")
plt.legend()
plt.show()











