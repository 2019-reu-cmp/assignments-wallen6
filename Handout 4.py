# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:57:05 2019

@author: winte
"""

"""
1:  Strings and lists are similar in that they both contain a series of 
    data.
    Strings and lists are different in that lists can contain any type 
    of data and lists can only contain characters.
    
2:  They can cut down the time the code takes to run, and they are 
    easier and faster to write.
 
    """
#Question 3
try: 
    import matplotlib as plt
except Exception as e: 
    print("matplotlib is not installed!", e) 
else: 
    print('matplotlib', plt.__version__ ) 

#Question 4
import numpy as np

a = (1,3,5)
b = (2,4,6)

print('Dot Product with enumerate')
for i, num in enumerate(a):
    print(np.dot(a,b))

print('Dot Product with zip')
for A,B in zip(a, b):
    print(np.dot(a,b))