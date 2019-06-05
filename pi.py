#!/usr/bin/env python3
""" pi.py - 
"""
import math as m

def srinivasa(k):
    """
    a= (2*m.sqrt(2))/9801
    b= sum((m.factorial(4*k)*(1103 + 26390*k))/(((m.factorial(k))**4)*396**(4*k)))
    p= 1/(a*b)
    print(p)
"""
    return m.pi    


if __name__ == '__main__':
    iterations = 1
    print(srinivasa(iterations))
    
