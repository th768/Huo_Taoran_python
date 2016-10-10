# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:11:35 2016

Group C Homework3

@author: Taoran Huo
"""
#Overall comment: Good Exercise and comments.
'''
1. Search for the IRIS dataset on the internet. You should quickly find the UCI Machine Learning
repository. Instead of downloading the files, figure out how to directly load the files from the
internet into Python and add the column names using Python code instead of an editor.
'''

import pandas as pd #import pandas
a=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
              names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
              #read the url and add the column names


'''
2. Using Pandas, display the first ten and the last ten rows of the data.
'''
a.head(10) #use head function, displaying the first ten rows of the data
a.tail(10) #use tail function, displaying the last ten rows of the data


'''
3. Using Pandas, print simple location statistics (Count, Mean, STD, Min, 25%, 50%, 75%, MAX).
There is a single method call that will accomplish this.
'''
a.describe() #use describe function, printing simple location statistics


'''
4. Write a function that accepts a list of numbers that represent numbers of bins and, using
Pandas, plots a histogram for each of the numeric columns at each bin size. For example, if I call
your function with [10, 50, 100] as bin sizes, the function should plot 12 histograms (3 for each
numeric variable). Group the histograms by the column name.
'''
columnname = ['sepal length', 'sepal width', 'petal length',
          'petal width', 'class']
def plothist(list1):
    for col in columnname[0:4]: #use for loop, count the 0-4 columns
        for i in list1: #use for loop, count each bin size in list1
            a.hist(column = col, bins = i) #print the histgrams
           
plothist([10,50,100]) #example


'''
5. Plot a box plot for each of the numeric column.
'''
import matplotlib.pyplot as plot #import matplotlib
plot.figure('sepal length box') #creat an empty figure
a['sepal length'].plot.box() #use box plot function, plot sepal length's box plot
plot.figure('sepal width box') #creat an empty figure
a['sepal width'].plot.box() #use box plot function, plot sepal width's box plot
plot.figure('petal length box') #creat an empty figure
a['petal length'].plot.box() #use box plot function, plot petal length's box plot
plot.figure('petal width box') #creat an empty figure
a['petal width'].plot.box() #use box plot function, plot petal width's box plot


'''
6. Plot a bar chart for the nominal column.
'''
a['class'].value_counts().plot.bar() #count the names frequency of class and then plot a bar chart





