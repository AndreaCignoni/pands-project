# Analysis.py
# This program summarizes my researches Fisher’s Iris data set'
# grouping differnt variables in histograms and scatter plots
# Author: Andrea Cignoni

import pandas as pd

df = pd.read_csv("iris.csv", header=None)
df.columns= ['sepal_lenght','sepal_width','petal_lenght','petal_width','class']

print(df)
