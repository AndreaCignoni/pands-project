# Analysis.py
# This program summarizes my researches Fisher’s Iris data set'
# Author: Andrea Cignoni

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading and formatting the data set downloaded (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)

df = pd.read_csv("iris.csv", header=None,)
df.columns= ['sepal_length','sepal_width','petal_length','petal_width','class']

# this shows first and last five raws of all data  
# print (df)

# to display stats about data
# print (df.describe())

# basic info about data type
# print (df.info ())

# to display number of samples on each class
# print (df['class'].value_counts())

# Preprocessing the dataset: check for null values

# print (df.isnull().sum())

# HISTOGRAMS

# 1. Plotting sepal lengths

plt.figure(figsize = (10, 7))
x = df["sepal_length"]
  
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")

plt.show()

# 2. Plotting sepal width

plt.figure(figsize = (10, 7))
x = df["sepal_width"]
  
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
  
plt.show()

# 3. Plotting petal length

plt.figure(figsize = (10, 7))
x = df['petal_length']

plt.hist(x, bins = 20, color = "blue")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")

plt.show()

# 4. Plotting petal width

plt.figure(figsize = (10, 7))
x = df['petal_width']

plt.hist(x, bins = 20, color = "blue")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")

plt.show()

# SCATTERPLOTS

# select setosa and versicolor and virginica
y = df.iloc[0:150, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)

# 1. Sepal and petal length

X = df.iloc[0:150, [0, 2]].values

# scaterplot lenght data
plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker='o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Versicolor')

plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')

# plt.show()

# 2. Sepal and petal width

X = df.iloc[0:150, [1, 3]].values

# scatterplot sepal and petal width data
plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker= 'o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Versicolor')

plt.xlabel('Sepal width [cm]')
plt.ylabel('Petal width [cm]')
plt.legend(loc='upper right')

# plt.show()

# 3. Petal width and length

X = df.iloc[0:150, [2, 3]].values

# scatterplot petal width and length data
plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker= 'o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Versicolor')

plt.xlabel('Petal length [cm]')
plt.ylabel('Petal width [cm]')
plt.legend(loc='upper left')

plt.show()

# 4. Sepal width and length

X = df.iloc[0:150, [0, 1]].values

# scatterplot sepal width and length data
plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker= 'o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Versicolor')

plt.xlabel('Sepal length [cm]')
plt.ylabel('Sepal width [cm]')
plt.legend(loc='upper right')

plt.show()