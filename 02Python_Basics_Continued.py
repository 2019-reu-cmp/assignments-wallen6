# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:40:31 2019

@author: winte
"""

"""
Question 1: 10**-3: 10, 10**-6: 20, and 10**-9: 30
        The program will bisect as long as the error>tolerance.
        Therefore, the smaller the tolerance is the longer it takes the error 
        decrease to the tolerance.

Question 2: You could define a new function. Then add the necessary computation
            into the rest of the code. For instance, define a new function
            for sin(x)-x. Then, add in the math to the code. Then the code 
            will output the iterations for both cos and sin.
    
Question 3: The difference between lists and tuples:
            lists can be changed and tuples cannot be
            
            The difference between dictionaries and tuples:
            Dictionaries are mutable and tuples are not
                
            The difference between sets and dictionaries:    
            Dictionaries are the standard mapping type 
            and a set is an unordered collection of hashable objects
            
            Cases of use:
            lists: To store similar items
            tuples:To allow storage in a set
            dictionaries: compare value
            sets: Removing duplicates from a sequence
            
Question 4: if (type(x==list))
                print(list)
            if (type(x != list))
                print(not list)