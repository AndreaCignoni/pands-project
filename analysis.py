# Analysis.py
# This program summarizes my researches Fisher’s Iris data set'
# Author: Andrea Cignoni

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the Fisher's data set from the file downloaded (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)

df = pd.read_csv("iris.csv", header=None,)
df.columns= ['sepal_lenght','sepal_width','petal_lenght','petal_width','class']

# to display stats about data

# df.describe()

# basic info about data type
# df.info ()

# to display number of samples on each class
# df['class'].value_counts()

# Preprocessing the dataset: check for null values
# df.isnull().sum()

# grouping differnt variables in histograms

# select setosa and versicolor and virginica
y = df.iloc[0:150, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)

# extract sepal length and petal length
X = df.iloc[0:150, [0, 2]].values

# plot data
plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker='o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Versicolor')

plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')

plt.show()


