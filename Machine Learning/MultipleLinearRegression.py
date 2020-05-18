#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 05:36:03 2020

@author: eneskuralay
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Multiple_Linear_Regression.csv", sep=";")

x = df.iloc[:,[0,2]].values
y = df.maas.values.reshape(-1,1)


multiple_lin_reg = LinearRegression()

multiple_lin_reg.fit(x,y)


print("b0: ",multiple_lin_reg.intercept_)

print("b1,b2: ", multiple_lin_reg.coef_)

# predict

print(multiple_lin_reg.predict(np.array([[10,35],[5,35]])))