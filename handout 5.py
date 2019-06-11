# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:26:18 2019

@author: winte
"""

"""
Handout 5

1:  Arrays can be used for computation without looping and lists cannot. 
    For instance, an array can be multiplied by 2 and all the numbers 
    will be doubled. This is not possible with a list.

2:  All elements of the array are affected individually.
    
3:  A specific axis must be indicated for the statistics functions.
    To make them work differently, you can indicate a different
    axis.
    
    """

#Question 4
import matplotlib.pyplot as plt
import pandas as pd
sun= pd.read_csv('sunspots.csv')
columns=['Month','Sunspots']
sun.columns=columns
x=sun.Sunspots
plt.hist(x,100,facecolor='blue', alpha=0.5,ec='black')
plt.ylabel('Number of Sunspots')
plt.xlabel('Strength of Sunspots')






