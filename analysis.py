# Analysis.py
# This program summarizes my researches Fisher’s Iris data set'
# grouping differnt variables in histograms and scatter plots
# Author: Andrea Cignoni

import pandas as pd
import numpy as pd
import os
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("iris.csv", header=None)
df.columns= ['sepal_lenght','sepal_width','petal_lenght','petal_width','class']

print(df)

'''
7. Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica 
'''

def histogram():

    # group data by species
    setosa = df[df['class'] == 'Iris-setosa']['petal_length']
    versicolor = df[df['class'] == 'Iris-versicolor']['petal_length']
    virginica = df[df['class'] == 'Iris-virginica']['petal_length']

    # plot histograms
    plt.hist(setosa, alpha=0.5, label='setosa')
    plt.hist(versicolor, alpha=0.5, label='versicolor')
    plt.hist(virginica, alpha=0.5, label='virginica')

    plt.legend(loc='upper right')
    plt.title('Petal Length Histogram')
    plt.xlabel('Petal Length')
    plt.ylabel('Frequency')
    plt.show()


# scatter and regression analysis
def analysis(first, second):
    plt.scatter(df[str(first)], df[str(second)])
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.show()

    x = df['sepal_length']
    y = df['petal_length']

    # slope, y-intercept of the regression line
    m, b = np.polyfit(x, y, 1)
    print('Slope:', m)
    print('Y-Intercept:', b)

    # regression line to the scatter plot.
    plt.scatter(x, y)
    plt.plot(x, m*x + b, color='red')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.show()

if __name__ == '__main__':

    histogram()
    analysis('sepal_length', 'petal_length')   

