<h1 align="center">

# *pands-project*
# **FISHER'S IRIS DATA SET ANALYSIS**
</h1>
<p align="justify">

The DATA file containing the reknown and long-studied **Fisher's Iris data set** have been downloaded from [www.archive.ics.uci.edu](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/). DATA files are used by a few software in order to store data specializing in statistical analysis and data mining and they can be either binary files or text files. In the text file, the newline character is converted to carriage-return/linefeed before being written to the disk and content written is human readable. On the contrary, in binary files, conversion of newline to carriage-return and linefeed does not take place and content is not human readable and looks like encrypted content. In order to find out which cathegory the DATA file downloaded belonged to and proceed to convert it accordingly, I have opened the data set in a .txt format. Since the content appeared readable and structured so that a comma separated individual items and each record was on a new line just as the standard pattern of a CSV tabular disposition, I have proceeded to open it as such in Python and imported the **Pandas** module to start my analysis.  
The data set contains 3 classes of 50 instances each, where each class refers to a type of Iris plant. One plant is linearly separable from the other 2; the latter are not separable from each other. Attribute information:
1. sepal length in cm;
2. sepal width in cm;
3. petal lenght in cm;
4. class: Iris Setosa; Iris Versicolour; Iris Virginica
</p>