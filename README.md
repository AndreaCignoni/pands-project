<div align="center">

# *pands-project*
# **FISHER'S IRIS DATA SET ANALYSIS**
</div>

<div align="justify">

In 1936, Sir Ronald Aylmer Fisher (17 February 1890 – 29 July 1962), the already renown British statistician and geneticist,  published a report titled “The Use of Multiple Measurements in Taxonomic Problems” in the journal Annals of Eugenics where his Iris flower data set was proposed as an example of discriminant analysis and as a method to predict qualitative values. He used it to distinguish the different species of Iris flowers from each other using the combination of the four measurement variables in the data set: *petal length*, *petal width*, *sepal length* and *sepal width*.  
The Iris dataset consists of 150 instances with 50 plants each of three classes of Iris plant, namely *Iris versicolor*, *Iris virginica* and *Iris setosa*. Sir Ronald Fisher summarised his studies in a diagram where he developed a discriminant function that performed well in discriminating between these species. However, as shown in the below picture, the three species of Iris are very similar and it is, therefore, very interesting to note how the different species characterization can be drawn from a statistical perspective.
<div align="center">
    <img src="/screenshots/screen1.jpg" width="400px"</img> 

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/main/Iris.png)

</div>

Starting from a classification problem, namely how to distinguish the three species starting from their measurements, my analysis plots the similarities and the differences of the three species shaping each flower's characteristics on graphs and giving a mathematical reconstruction of their visual differentiation. The histograms are used to summarize their main features while the scatterplots visually highlight how each individual flower develop its own peculiarities. I then pass to reproduce their discriminant factor on a logic point of you as my aim is to outline the measurement ranges characteristic to each species and to show how to recognize every specific flower on a mathematic point of view. Through my explanatory data analysis, I finally attribute a distinction principle that allows to predict the flower class from its attributes (its measurements). My work tries to reproduce the demostrations shown on the following lecture on [YouTube](https://www.youtube.com/watch?v=FLuqwQgSBDw).  

**LIBRARIES IMPORTED**

The DATA file containing the long-studied **Fisher's Iris data set** has been downloaded from [archive.ics.uci.edu](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/) where it is found in the DATA format. The first problem is to open it and visualize all its information. DATA files are used by a few software in order to store data specializing in statistical analysis and data mining and they can be either *binary files* or *text files*. In *the text file*, the newline character is converted to carriage-return/linefeed before being written to the disk and the content written is human readable. On the contrary, in *binary files*, conversion of newline to carriage-return and linefeed does not take place. The content is not human readable and looks like encrypted content. In order to find out which of the categories the DATA file downloaded belonged to and, consequently, converting it, I have opened the data set in a .txt format. Since the information appears readable and structured just as the standard pattern of a CSV tabular disposition (a comma separates individual items and each record is on a new line), I have proceeded to open it as such in Python and, then, I have imported the modules that help me develop my analysis on the data set: **Pandas**; **Matplotlib**; **Numpy**; **Seaborn**.

**Pandas**

*Pandas* is an open source Python package that is most widely used for data science/data analysis and machine learning tasks. *Pandas* makes it simple to do many of the time consuming, repetitive tasks associated with working with data, including: data cleansing, data fill, data normalization, merges and joins, data visualization, statistical analysis, data inspection, loading and saving data and much more. Here, I am using this module mainly to indexing the data frame, to manipulate it and to extract the sorted information from specified columns and rows.

**Matplotlib**

*Matplotlib* is a Python library used to create 2D graphs and plots by using Python scripts. It has a module named *pyplot* which makes things easy for plotting by providing feature to control line styles, font properties, formatting axes etc. It supports a very wide variety of graphs and plots namely - histogram, bar charts, power spectra, error charts etc. 

**Numpy**

*Matplotlib* is used along with *NumPy* to provide an environment with an effective and fast numeric computing. *Numpy* furnishes a multidimensional array object and various derived objects (such as masked arrays and matrices).

**Seaborn**

Lastly, in order to clearly display through *pair plots* my conclusion, I have imported *Seaborn*. This library is built on top of the *Matplotlib* data visualization library and can perform the exploratory analysis that fits best to show the result of my searches.


**LOADING THE SET**

In order to load the data frame, manipulating its information and output a summary of it to display an overview of its main features to a *text file*, I have expanded my knowledge of *Pandas* and its functions following the instruction contained in [pandas.pydata.org](https://pandas.pydata.org/docs/user_guide/10min.html). As already pointed out, the data set contains 3 classes of flowers and 50 instances of each species, where each class refers to a type of Iris plant and the 4 types of observations which makes a total of 1 dependent variable – labelled in my work as the *class*- and 4 independent variables – labelled here ‘sepal_length’, ‘sepal width’, ‘petal length’ and ‘petal width’. These attributes are expressed as follows:

1. sepal length in cm;
2. sepal width in cm;
3. petal lenght in cm;
4. petal width in cm;
5. class: Iris Setosa; Iris Versicolour; Iris Virginica

<div align="center">

![ScreenShot](https://github.com/AndreaCignoni/mywork/blob/908532f4e05af5576c4802e2b1924e260c94269e/IndexingDataFrame.PNG)

</div>

**CREATING A SUMMARY OF EACH VARIABLES**

In order to display in a user-friendly format the content of the dataset, I have grouped the output of different *Pandas* functions in a text file called *irisDatasetSummary.txt* which contains the most relevant information of the data collection.  This brief summary starts with the information extracted from the *Iris Data Set* with the *df.describe()* method that shows the sum of *count*, *mean*, *std*, *min* and *maximum* of all values.  To visualize the number of samples of each class, the set is processed with the *df['class'].value_count* function. Lastly, in order to group the measurements by their mean values and the correlation between the values of the three species, I have sorted the information with the *groupby().mean()* and *groupby().corr()* methods.

<div align="text-align: right">

+ *df.describe()*

![ScreenShot](https://github.com/AndreaCignoni/mywork/blob/908532f4e05af5576c4802e2b1924e260c94269e/DataFrameDescribe.PNG)

- *df['class'].value_counts()*

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/908532f4e05af5576c4802e2b1924e260c94269e/ClassCounts.PNG)

* *df.groupby('class').mean* and *groupby('class').corr()*

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/a6c8e3fc2a5e16921701f1c7c8e16647cfcd3b21/MeanValues.PNG)

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/a6c8e3fc2a5e16921701f1c7c8e16647cfcd3b21/Correlation.PNG)

</div>

**PREPROCESSING THE DATA SET**

Before proceeding to my actual analysis, I have *preprocessed* the data contained in the *Iris data set* in order to remove missing or inconsistent data values resulting from human or computer error. *Preprocessing data* can significantly improve the accuracy and quality of a dataset, making it more reliable. This procedure makes data consistent and helps to get rid of unhelpful parts of the data transforming the information into a format that is more easily and effectively processed in data mining, machine learning and other data science tasks. This procedure was performed with the following function:

*check for null values*
- *df.isnull().sum()* = no null values

<div align="text-align: right">

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/908532f4e05af5576c4802e2b1924e260c94269e/PreprocessingData.PNG)
</div>

**EXPLORATORY DATA ANALYSIS** 

One plant is linearly separable from the other 2; the latter are not easily separable from each other. This is the issue I have planned to solve with my work and that clearly emerges from the very first plots I have generated. Once graphically represented the flowers, I have then passed to look for a discriminant principle that allows to predict from the independent variable the dependent variable.  My study is, therefore, divided into two parts: the first where the *iris setosa* peculiarity is outlined in comparison to the other two species; the second where I trace a distinction as clear as possible between the other two classes, the *iris versicolor* and the *iris virginica*. In fact, as already stated, while a discrimination between the *iris setosa* and the other two plants emerges from the first set of plots, drawing a rule that can be applied to differentiate the *iris versicolor* from *the virginica* is quite a more challenging task. In the end, this is the objective of my analysis: **to classify a new flower as belonging to one of the three species starting from a set of its 4 types of measurements**.

1. **HOW *IRIS SETOSA* CHARACTERISTICS EASILY DIFFERECIATE FROM THE OTHER TWO**

My analysis, then, starts showing and comparing the three species through histograms and scatterplots. The **histograms** show the *frequency distribution* of a data set and in this case help to visualize which class of flower presents data in *normal distribution* (a bell shaped curve) and which not. This kind of representation draws attention to the spikes appearing in the graphs. One key concept to take into account when working with histograms is the idea of *bins* - how many parts the total range of the data set is divided into. Changing the number of *bins* in a histogram does not change the data set. It only changes the appearance of the data in the histogram. The histogram method can accept a few different arguments, but the most important two are:

**x**: the data set to be displayed within the histogram;  
**bins**: the number of bins that the histogram should be divided into.

The four histograms below are based on 2 variables each: one measurement and class of species. The three flowers are plotted using the transparency technique which allows where the species have more points in commons. When creating a plot of a graph, by default, *Matplotlib* have the default transparency set at 1. However, this transparency can be adjusted using the alpha attribute at 0.5, as in my case, or at 0.25. My main point of reference for plotting histograms on the Fisher's Iris data set is [nickmccullum](https://www.nickmccullum.com/python-visualization/histogram/).

<div align="center">

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/96002dd96e37b61c92de23a1635a2ee4b6cd5e8e/Petal_Length.png)


![Screenshot](https://github.com/AndreaCignoni/mywork/blob/96002dd96e37b61c92de23a1635a2ee4b6cd5e8e/Petal_Width.png)


![Screenshot](https://github.com/AndreaCignoni/mywork/blob/96002dd96e37b61c92de23a1635a2ee4b6cd5e8e/Sepal_Length.png)


![Screenshot](https://github.com/AndreaCignoni/mywork/blob/7c42d117895d01509536d94a37e90c404d34c55f/Sepal_Width.png)

</div>

As highlighted by the above four graphs, the shapes of the *iris versicolor* and of the *iris virginica* are almost overlying while the *iris setosa* stands nearly on its own in every histogram in every case. Therefore, **we can easily distinguish an *iris setosa* from the other two species plotting a single set of measures with an histogram**.  
    **Scatterplots** are developped attributing a different colour to each class and considering their petal/sepal width on the y axis and length on the x axis. In this way the similarities and differences between the two pairs of variables (lenght and width/ petals and sepals) are described in relation to the three species.
The patterns or correlations can be either:
*Linear or Nonlinear*: A linear correlation forms a straight line in its data points while a non linear correlation might have a curve or other form within the data points
*Strong or Weak*: A strong correlation has data points close together while a week correlation has data points that are further apart
*Positive or Negative*: A positive correlation points up (both *x* and *y* values increasing) while a negative correlation points down (*x* and *y* values decreasing)

My point of reference here for scatterplots and their usage is [visme](https://visme.co/blog/scatter-plot/)

+ Sepal width and legth displayed.
<div align="center">

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/908532f4e05af5576c4802e2b1924e260c94269e/ScatterSepalLengthWidth.png)
</div>

* Petal length and width displayed.
<div align="center">

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/908532f4e05af5576c4802e2b1924e260c94269e/ScatterPetalLengthWidth.png)
</div>

- Sepal  and petal width compared.
<div align="center">

![Scatterplot](https://github.com/AndreaCignoni/mywork/blob/908532f4e05af5576c4802e2b1924e260c94269e/ScatterPlotWidth.png)
</div>

* Petal and sepal legth compared.
<div align="center">

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/908532f4e05af5576c4802e2b1924e260c94269e/ScatterPlotLength.png)
</div>

</div>
