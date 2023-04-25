# Analysis.py
# This program summarizes my researches Fisher’s Iris data set'
# Author: Andrea Cignoni

import pandas as pd
import matplotlib as plt

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
plt.df['sepal_lenght'].hist()
plt.show()


