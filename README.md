<div align="center">

# *pands-project*
# **FISHER'S IRIS DATA SET ANALYSIS**
</div>

<div align="justify">

In 1936, Sir Ronald Aylmer Fisher (17 February 1890 – 29 July 1962), the already reknown British statistician and geneticist   published a report titled “The Use of Multiple Measurements in Taxonomic Problems” in the journal Annals of Eugenics where his Iris flower data set was proposed as an example of discriminant analysis and as a method to predict qualitative values. He used it to distinguish the different species of Iris flowers from each other using the combination of the four measurement variables in the data set: *petal lenght*, *petal width*, *sepal legth* and *sepal width*.  
The Iris dataset consists of 150 instances with 50 plants each of three classes of Iris plant, namely *Iris versicolor*, *Iris virginica* and *Iris setosa*. Sir Ronald Fisher summarised his studies in a diagram where he developed a discriminant function that performed well in discriminating between these species. However, as shown in the below picture, the three species of Iris are very similar and it is, therefore, very interesting to note how the different species characterization can be drawn from a statistical perspective.
<div align="center">
    <img src="/screenshots/screen1.jpg" width="400px"</img> 

![Screenshot](https://github.com/AndreaCignoni/mywork/blob/main/Iris.png)

</div>
My analysis will then plot the similarities and the differences of the three species starting from this values collection and I will shape each flower's characteristics on ghraphs giving a mathematical reconstruction of their visual differentiation. The histograms will be used to summarize their main feactures while the scatterplots will visually highlight how each individual flower develop its own peculiarities. I will finally pass to reproduce their discriminant factor on a logic point of you. My aim is to outline the measurement ranges characteristic to each species and show how to recognize every specific flower on a mathematic point of view.

**LOADING DATASET**

The DATA file containing the reknown and long-studied **Fisher's Iris data set** have been downloaded from [www.archive.ics.uci.edu](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/). DATA files are used by a few software in order to store data specializing in statistical analysis and data mining and they can be either binary files or text files. In the text file, the newline character is converted to carriage-return/linefeed before being written to the disk and content written is human readable. On the contrary, in binary files, conversion of newline to carriage-return and linefeed does not take place and content is not human readable and looks like encrypted content. In order to find out which cathegory the DATA file downloaded belonged to and proceed to convert it accordingly, I have opened the data set in a .txt format. Since the content appeared readable and structured so that a comma separated individual items and each record was on a new line just as the standard pattern of a CSV tabular disposition, I have proceeded to open it as such in Python and imported the modules that allowed me to start the analysis on the data set: **Pandas**; **Matplotlib**;**Numpy**.

**Pandas**

*Pandas* is an open source Python package that is most widely used for data science/data analysis and machine learning tasks. Pandas makes it simple to do many of the time consuming, repetitive tasks associated with working with data, including: data cleansing, data fill, data normalization, merges and joins, data visualization,statistical analysis, data inspection, loading and saving data and much more.

**Matplotlib**

*Matplotlib* is a Python library used to create 2D graphs and plots by using Python scripts. It has a module named *pyplot* which makes things easy for plotting by providing feature to control line styles, font properties, formatting axes etc. It supports a very wide variety of graphs and plots namely - histogram, bar charts, power spectra, error charts etc. 

**Numpy**

*Matplotlib* is used along with *NumPy* to provide an environment with an effective and fast numeric computing. *Numpy* provides a multidimensional array object and various derived objects (such as masked arrays and matrices).

**LOADING THE SET**

As already pointed out, the data set contains 3 classes of 50 instances each, where each class refers to a type of Iris plant. One plant is linearly separable from the other 2; the latter are not separable from each other. Attribute information:
1. sepal length in cm;
2. sepal width in cm;
3. petal lenght in cm;
4. petal width in cm;
4. class: Iris Setosa; Iris Versicolour; Iris Virginica

In order to display stats about data set, I have used the function *df.describe()* that shows the sum of *count*, *mean*, *std*, *min* and *maximum* in cm of each sepal and petal, lenght and width.The type of data stored in the file showed that the measure in cm were stored in *float64* format and the species were objects. This information were retrieved with function *df.info*. To visualize the number of samples of each class is *df['class'].value_count*. For each class the data set presents 50 samples

**PREPROCESSING THE DATA SET**

*Preprocessing data* removes missing or inconsistent data values resulting from human or computer error, which can improve the accuracy and quality of a dataset, making it more reliable. It makes data consistent. This helps to get rid of unhelpful parts of the data and transforms the data into a format that is more easily and effectively processed in data mining, machine learning and other data science tasks. This procedure was performed with the following functions:

*check for null values*
df.isnull().sum()= no null values

**EXPLORATORY DATA SET** 
The **histograms** show the *frequency distribution* of a data set and in this case help to visualize which class of flower presents data in *normal distribution* (a bell shaped curve) and which not. Spikes in the graphs variations to be pointed out.

df['SepalLenghtCm'].hist()
df['SepalWidthCm'].hist()
df['PetalLenghtCm'].hist()
df['PetalWidthCm'].hist()

The **scatterplots** attributing a different colour for each class and considering their petal/sepal width on the y axis and length on the x axis describe correlations between the two pairs of variables (lenght and width/ petals and sepals) of the three species.
The patterns or correlations can be either:
**Linear or Nonlinear**: A linear correlation forms a straight line in its data points while a non linear correlation might have a curve or other form within the data points
**Strong or Weak**: A strong correlation has data points close together while a week correlation has data points that are further apart
**Positive or Negative**: A positive correlation points up (both *x* and *y* values increasing) while a negative correlation points down (*x* and *y* values decreasing)

My point of reference here for scatterplots and their usage is [www.visme.co](https://visme.co/blog/scatter-plot/)



</div>
