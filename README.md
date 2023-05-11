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

My analysis, then, starts showing and comparing the three species through histograms and scatterplots. The **histograms** show the *frequency distribution* of a data set and, in this case, help to visualize which class of flower presents data in *normal distribution* (a bell shaped curve) and which not. This kind of representation draws attention to the spikes appearing in the graphs. One key concept to take into account when working with histograms is the idea of *bins* - how many parts the total range of the data set is divided into. Changing the number of *bins* in a histogram does not change the data set. It only changes the appearance of the data in the histogram. The histogram method can accept a few different arguments, but the most important two are:

**x**: the data set to be displayed within the histogram;  
**bins**: the number of bins that the histogram should be divided into.

The four histograms below are based on 2 variables each: one measurement and class of species. The three flowers are plotted using the transparency technique which clearly display where the species have more features in common. *Iris setosa* is plotted in red, *iris versicolor* in green and *iris virginica* in red. When creating a plot of a graph, *Matplotlib* have the default transparency set at 1. However, this transparency can be adjusted using the *alpha* attribute at 0.5, as in my case, or at 0.25. My main point of reference for plotting histograms on the Fisher's Iris data set is [nickmccullum](https://www.nickmccullum.com/python-visualization/histogram/).

<div align="center">

![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/50345098de351dcba6c3066caef594e990c08046/Petal_Length.png)


![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/50345098de351dcba6c3066caef594e990c08046/Petal_Width.png)


![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/40e2dd861b2d92842600b8b45aa22c25bbf00320/Sepal_Length.png)


![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/40e2dd861b2d92842600b8b45aa22c25bbf00320/Sepal_Width.png)

</div>

As highlighted by the above four graphs, the shapes of the *iris versicolor* and of the *iris virginica* are almost always overlying each other while the *iris setosa* constantly stands on its own. Therefore, with the use of an histogram we can easily discriminate an *iris setosa* from the other two species using one single variables of the measurements.
But how can we distinguish an *iris versicolor* from an *iris virginica* or viceversa? To answer this question, the set of misurements must be 2 and I have recurred to the help of *scatterplots* to display a two dimension graph.

2. ***IRIS VERSICOLOR* AND *IRIS VIRGINICA*’S DISCRIMINATION**

As for the *histograms*, I have attributed a different colour to each class of plant: blue for the *iris setosa*,  green for the *iris versicolor* and red for the *iris virginica* respectively. In this way, the similarities and differences between the two pairs of variables (length and width/ petals and sepals) can be clearly displayed for each of the three species. The patterns or correlations created are either *Linear* or *Nonlinear*, *Strong* or *Weak*, *Positive* or *Negative*: 
•	*Linear* or *Nonlinear*: a *linear correlation* forms a straight line in its data points while a *non linear* correlation might have a curve or other form within the data points;
•	*Strong* or *Weak*: a *strong* correlation has data points close together while a *weak* correlation has data points that are further apart;
•	*Positive* or *Negative*: a *positive*e correlation points up (both x and y values increasing) while a *negative* correlation points down (x and y values decreasing).  
The following scatterplots show that a *linear* correlation separate the *iris setosa* from the other two species that are always *non linearly* separated. Therefore, in order to discriminate the *iris versicolor* from the *iris virginica* we need to recur to the second discrimination mentioned above, namely searching the graph where the patterns plotted are *weaker* and the *iris versicolor* and the *iris virginica* are more apart. 

+ Sepal width and length displayed;
<div align="center">

![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/dfb0e62aa6a4dd735bdfb7559febee03402f44b0/SepalLengthWidth.png)
</div>

* Petal length and width displayed;
<div align="center">

![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/b58ed4ae833ee5a392e0c0e2f5f0931a8b76dc70/PetalLengthWidth.png)
</div>

- Sepal and petal width displayed;
<div align="center">

![Scatterplot](https://github.com/AndreaCignoni/pands-project/blob/b7fc59b5dcad86110cc8297bbbcaada4cc4b6b7b/PetalSepalWidth.png)
</div>

+ Petal and sepal length displayed;
<div align="center">

![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/78e075090160404148053bd550e5101deb697024/PetalSepalLength.png)
</div>

- Sepal length and petal width displayed;
<div align="center">

![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/bfced1b2a94b372551ed265ab76abdfca48b2b94/SepalLengthPetalWidth.png)
</div>

* Petal length and sepal width displayed;
<div align="center">

![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/1099840cc4b101f026c7f73da87ee3e65bedeb02/SepalWidthPetalLength.png)
</div>

As can be easily noticed, the second *scatterplot*, where the dimensions taken into consideration are the *petal length* and the *petal width*, is the one that describe a clearer distinction between the two classes of flowers. However, to develop the necessary system of reference to assess a form of principle to isolate one class of flower from the other two, I have drawn on *pairs plot* and its grids. For plotting *scatterplots* and comprehend their usage, my source here has been [visme](https://visme.co/blog/scatter-plot/).  
The *pairs plot* below display a global overview of all the plots so far shown and,  since there are 4 measurements, a 4x4 plot has been created with 6 bidimensional mirroring *scatterplots* and 4 one-dimensional histograms. The white grid on which the data are deployed allow a deeper analysis of the above indicated *scatterplot* - the one generated over the *petal length* and the *petal  width* measures- giving the necessary landmarks to  isolate the *iris virginica* from the *iris versicolor*.

<div align="center">

![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/40e2dd861b2d92842600b8b45aa22c25bbf00320/PairPlots.png)
</div>

In order to generate the above plot and learn the most relevant *Seaborn*'s features, I have followed [seaborn.pydata.org](https://seaborn.pydata.org/generated/seaborn.pairplot.html). The *Seaborn Pairplot* function is used to plot pairwise relationships between variables within a dataset. The pairs plot builds on two basic figures, the *histogram* and the *scatter plot*. The *histogram* on the diagonal allows us to see the distribution of a single variable while the *scatter plots* on the upper and lower triangles show the relationship (or lack thereof) between two variables. This creates a nice visualisation and helps understand the data by summarising the whole *Fisher's Iris Data Set* in a single figure.  
The *pairplot* method can create also a grid of axes such that each variable in data are shared in the y-axis across a single row and in the x-axis across a single column. At this point, I can pass to examine the *scatterplot* with the *weaker* correlation between the *iris virginica* and *iris versicolor*.

<div align="center">

![Screenshot](https://github.com/AndreaCignoni/pands-project/blob/4ab8abec43a2a4162c99d2d534049a08ed677c59/Focus.png)
</div>

**Using the measures on y, x axis and the lines dividing data on the above *scatterplot* we can build a simple model through a 3 if-else conditions statement to classify each flower type which is also the aim of my research:**  

1. **IF** PETAL WIDTH AND PETAL LENGTH ≤ THAN 1 IS *SETOSA*
2. **ELIF** PETAL WIDTH IS ≤ THAN 2 CM AND ≥ THAN 1 CM AND 
PETAL LENGTH IS ≤ THAN 5 AND ≥ THAN 2.5 CM THEN IS *VERSICOLOR*
3. **ELSE** IS *VIRGINICA*

This Boolean expression is far from perfect and the error margin is still high. In fact, as the above plot shows, the *iris versicolor* and the *iris virginica*'s data are still intertwined and not so easily separable from one and another. However, this demonstration is meant to give a partial explanation of why this dataset, created in 1936, has been so long studied and why it is still used to implement some of the commonly used algorithms in machine learning. My efforts through this analysis have been directed to recognize the patterns which emerge from the iris measurements and, in the end, once identified a possible principle for discriminating the three species, use it to make predictions about those data with a reasonable margin of error.  
</div>