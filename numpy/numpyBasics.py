#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:25:42 2020

@author: eneskuralay
"""

import numpy as np 


array = np.array([1,2,3,4,5,6,7,8,9,10]) # 1 * 10 Vector
print(array)
print(array.shape)

a = array.reshape(2,5)
print(a)
print(a.shape)

print("dimension: ", a.ndim)


print("data type : ", a.dtype.name)

print("size : ", a.size)

print("type : ",type(a))


array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6]])

print(array1.shape)

zeros = np.zeros((3,4))
zeros[0,0] = 5

print(zeros)

ones = np.ones((3,4))
ones[0,0] = 3

print(ones)

print(np.empty((2,4)))

arange = np.arange(10,50,1.5)
print(arange, " " , arange.shape )

linspace = np.linspace(10,50,27)
print(linspace)

# %% numpy basics operations

print("-"*30)

a = np.array([1,2,3,4])

b = np.array([5,6,7,8])

print(a+b)
print(a-b)
print(a**2)
print(np.sin(a))
print(a<2)


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

print(a*b)
print(a.dot(b.T))

print(np.exp(a))

a = np.random.random((5,5))
print(a)

print(a.sum(axis=0))
print(a.sum(axis=1))

print(np.sqrt(a))
print(np.square(a))

print(np.add(a,a))

# %%  indexing and slicing

print("-"*30)

array = np.array([1,2,3,4,5,6,7])

print(array[0])
print(array[0:4])

reverse_array = array[::-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1])
print(array1[:,1])

print(array1[1,1:4])


print(array1[1,:])
print(array1[:,-1])

# %% shape manipulation

print("-"*30)

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)

#flatten

a = array.ravel()
print(a)

array2 = a.reshape(3,3)
print(array2)

arrayT = array2.T
print(arrayT)
print(array.shape)

array5 = np.array([[1,2],[3,4],[5,6]])

array5.reshape(2,3)
print(array5)

array5.resize((2,3))
print(array5)

# %% stacking arrays
print("-"*30)

array1 = np.array([[1,2],[3,4]])


array2 = np.array([[-1,-2],[-3,-4]])

# vertical stack

array3 = np.vstack((array1,array2))

print(array3)
# horizontal stack

array4 = np.hstack((array1,array2))
print(array4)


print("-"*30)

list1 = [1,2,3,4]

array = np.array(array)

print(array)

list2 = list(array)

















