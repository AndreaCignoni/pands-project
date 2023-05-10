# Analysis.py
# This program summarizes my researches on 'Fisher’s Iris data set'
# My aim is to display how the three species of flowers differentiate themselves on a statistical point of view
# I will outline a discriminanting principle to predict a species from its set of measurement
# Author: Andrea Cignoni

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reading and formatting the data set downloaded (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)

df = pd.read_csv("iris.csv", header=None,)

# Creating a file called *irisDatasetSummary.txt* to summarize the basic information of the dataset
print("This dataset contains 5 variables, 4 measurements and class of flower, for 150 observations", file =open("irisDatasetSummary.txt", "w"))

print("\n","Below are shown the first and the last five raws of the dataset.", file=open("irisDatasetSummary.txt", "a"))
df.columns= ['sepal_length','sepal_width','petal_length','petal_width','class']
# this shows first and last five raws of all data  
print(df, file=open("irisDatasetSummary.txt", "a"))
print("\n","These are the main statistical information of the dataset:","\n",file=open("irisDatasetSummary.txt","a"))
# to display stats about data
print(df.describe(),file=open("irisDatasetSummary.txt","a"))
# to display number of samples on each class
print("\n","Number of samples for each class:","\n",file=open("irisDatasetSummary.txt","a"))
print(df['class'].value_counts(),file=open("irisDatasetSummary.txt","a"))
# Grouping the mean values of the three species and showing their correlation
print("\n","The mean values of the three classes is as follows:","\n",file=open("irisDatasetSummary.txt","a"))
print(df.groupby('class').mean(),file=open("irisDatasetSummary.txt","a"))
print("\n","This is how the values are correlated:","\n",file=open("irisDatasetSummary.txt","a"))
print(df.groupby('class').corr(),file=open("irisDatasetSummary.txt","a"))
# Preprocessing the dataset: check for null values
print("\n","As shown below, no missing values were found in the raw file:","\n",file=open("irisDatasetSummary.txt","a"))
print(df.isnull().sum(),file=open("irisDatasetSummary.txt","a"))

# HISTOGRAMS
# Creating an histogram for each dimension which will be measured on the x axis
# Trasparency achieved with alpha attribute: the iris setosa species stands on its own while the other two species are overlaid in every graph

# 1. Plotting sepal lengths

# group data by species
setosa = df[df['class'] == 'Iris-setosa']['sepal_length']
versicolor = df[df['class'] == 'Iris-versicolor']['sepal_length']
virginica = df[df['class'] == 'Iris-virginica']['sepal_length']

# plot histogram
plt.hist(setosa, color='blue', alpha=0.5, label='setosa')
plt.hist(versicolor, color='green', alpha=0.5, label='versicolor')
plt.hist(virginica, color='red', alpha=0.5, label='virginica')

plt.legend(loc='upper right')
plt.title('Sepal Length Histogram')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# 2. Plotting sepal width

# group data by species
setosa = df[df['class'] == 'Iris-setosa']['sepal_width']
versicolor = df[df['class'] == 'Iris-versicolor']['sepal_width']
virginica = df[df['class'] == 'Iris-virginica']['sepal_width']

# plot histogram
plt.hist(setosa, color='blue', alpha=0.5, label='setosa')
plt.hist(versicolor, color='green', alpha=0.5, label='versicolor')
plt.hist(virginica, color='red', alpha=0.5, label='virginica')

plt.legend(loc='upper right')
plt.title('Sepal Width Histogram')
plt.xlabel('Sepal Width')
plt.ylabel('Frequency')
  
plt.show()

# 3. Plotting petal length

# group data by species
setosa = df[df['class'] == 'Iris-setosa']['petal_length']
versicolor = df[df['class'] == 'Iris-versicolor']['petal_length']
virginica = df[df['class'] == 'Iris-virginica']['petal_length']

# plot histogram
plt.hist(setosa, color='blue', alpha=0.5, label='setosa')
plt.hist(versicolor, color='green', alpha=0.5, label='versicolor')
plt.hist(virginica, color='red', alpha=0.5, label='virginica')

plt.legend(loc='upper right')
plt.title('Petal Length Histogram')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()


# 4. Plotting petal width

# group data by species
setosa = df[df['class'] == 'Iris-setosa']['petal_width']
versicolor = df[df['class'] == 'Iris-versicolor']['petal_width']
virginica = df[df['class'] == 'Iris-virginica']['petal_width']

# plot histogram
plt.hist(setosa, color ='blue', alpha=0.5, label='setosa')
plt.hist(versicolor, color='green', alpha=0.5, label='versicolor')
plt.hist(virginica, color='red', alpha=0.5, label='virginica')

plt.legend(loc='upper right')
plt.title('Petal Width Histogram')
plt.xlabel('Petal Width')
plt.ylabel('Frequency')
plt.show()

# SCATTERPLOTS
# Scatterplots used to graphically distinguish iris versicolor from iris virginica
# iris setosa remains segregated from the other two species as in the previous histograms
# Plotting all the 6 possible combination of 2 dimensions scatterplots to identify where the the iris versicolor and the iris virginica are more visibly distinguished

# select setosa and versicolor and virginica: 
y = df.iloc[0:150, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)

# 1. Sepal and petal length

X = df.iloc[0:150,[0, 2]].values

# selecting rows and distinguishing flowers by colours

plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker='o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Virginica')

# Generating scatterplot

plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')

plt.show()

# 2. Sepal and petal width

X = df.iloc[0:150,[1, 3]].values

# selecting rows and distinguishing flowers by colours

plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker= 'o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Virginica')

# Generating scatterplot

plt.xlabel('Sepal width [cm]')
plt.ylabel('Petal width [cm]')
plt.legend(loc='upper right')

plt.show()

# 3. Petal width and length

X = df.iloc[0:150,[2, 3]].values

# selecting rows and distinguishing flowers by colours

plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker= 'o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Virginica')

# Generating scatterplot

plt.xlabel('Petal length [cm]')
plt.ylabel('Petal width [cm]')
plt.legend(loc='upper left')

plt.show()

# 4. Sepal width and length

X = df.iloc[0:150,[0, 1]].values

# selecting rows and distinguishing flowers by colours

plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker= 'o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Virginica')

# Generating scatterplot

plt.xlabel('Sepal length [cm]')
plt.ylabel('Sepal width [cm]')
plt.legend(loc='upper right')

plt.show()

# 5. Petal length and sepal width

X = df.iloc[0:150,[1, 2]].values

# selecting rows and distinguishing flowers by colours

plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker= 'o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Virginica')

# Generating scatterplot

plt.xlabel('Petal length [cm]')
plt.ylabel('Sepal width [cm]')
plt.legend(loc='upper left')

plt.show()

# 6. Petal width and sepal length

X = df.iloc[0:150,[0, 3]].values

# selecting rows and distinguishing flowers by colours

plt.scatter(X[:50, 0], X[:50, 1],
            color='blue', marker= 'o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='green', marker='s', label='Versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1],
            color='red', marker='*', label='Virginica')

# Generating scatterplot

plt.xlabel('Petal width [cm]')
plt.ylabel('Sepal length [cm]')
plt.legend(loc='upper right')

plt.show()

# Pairwise scatter plots generated with Seaborn to achieve a global overview of all 6 combinations of the 2 dimensions graphs
# using a whitegrid pattern to establish a discrimination principle between iris virginica and iris versicolor

sns.set_style("whitegrid")
sns.pairplot(df, hue="class", palette= ["blue","green","red"], markers=["o","s","*"], height=1.5)
plt.show()

# Scatter plot based on petal length and width show a weaker correlation between iris virginica and iris versicolor
# Using measures on y, x axis and lines drawn on the above said scatterplot
# we can build a simple model through if-else conditions to classify the flower types:
# IF PETAL WIDTH IS ≤ TO 2 CM AND ≥ THAN 1 CM AND 
# PETAL LENGTH IS ≤ THAN 5 AND ≥ THAN 2.5 CM THEN IS VERSICOLOR