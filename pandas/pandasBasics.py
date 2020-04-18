#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 03:22:57 2020

@author: eneskuralay
"""

import pandas as pd 

dictionary = {"Name":["Ali","Veli","Ahmet","Emine","Ayşe"],
              "Age":[21,32,42,24,35],
              "Salary":[2500,3500,5000,4500,3700]
        }

dataframe1 = pd.DataFrame(dictionary)

head = dataframe1.head()
tail = dataframe1.tail()

print(dataframe1.columns)


print(dataframe1.info())


print(dataframe1.dtypes)

print(dataframe1.describe())

# %% indexing and slicing

print("-*"*30)

print(dataframe1["Age"])
print(dataframe1.Age)


dataframe1["new feature"] = [-1,-2,-3,-4,-5,]

print(dataframe1.loc[:,"Salary"])

print(dataframe1.loc[:3,"Salary"])

print(dataframe1.loc[:3,"Name":"Salary"])


print(dataframe1.loc[:3,["Name","Salary"]])

print(dataframe1.loc[::-1,:])


print(dataframe1.loc[:,:"Salary"])

print(dataframe1.loc[:,"Salary"])

print(dataframe1.iloc[:,2])


#%% Filtiring



filtre1 = dataframe1.Salary > 3500


filter_data = dataframe1[filtre1]

filtre2 = dataframe1.Age > 25

print(dataframe1[ filtre1 & filtre2 ])

print(dataframe1[dataframe1.Age > 40])




#%%   list comprehension

import numpy as np 

mean_salary = dataframe1.Salary.mean()

print(mean_salary)


mean_salary_np = np.mean(dataframe1.Salary)

print(mean_salary_np)

dataframe1["Salary_level"] = ["high" if mean_salary < each else "low" for each in dataframe1.Salary]

# =============================================================================


dataframe1["Salary level"] = ["high" if mean_salary < each else "low" for each in dataframe1.Salary]

dataframe1.columns = [each.lower() for each in dataframe1.columns]

dataframe1.columns = [each.split()[0] + "_" + each.split()[1] if (len(each.split())>1) else each for each in dataframe1.columns]

#%% drop and concatenating 



dataframe1.drop(["new_feature"],axis=1,inplace=True)


data1 = dataframe1.head()
data2 = dataframe1.tail()

data_concat = pd.concat([data1,data2],axis=0)

salary = dataframe1.salary
age = dataframe1.age

data_h_concat = pd.concat([salary,age],axis=1)

#%% transforming data

dataframe1["list_comp"] = [each*2 for each in dataframe1.age]

def multiply(age):
    
    return age * 2 

dataframe1["apply_method"] = dataframe1.age.apply(multiply)










