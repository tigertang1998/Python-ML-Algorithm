# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:05:31 2018

@author: TIGER
"""

import pandas as pd
import numpy as np


def J(theta, X, y):
    '''
    Args:
        X, with raws being each x sample data m*n (X is nparray)
        y, with raws being each y sample data m*1
        theta  n*1
    
    Returns:
        Cost of prediction by theta
    '''
    m = len(X)
    return (X*theta-y).T*(X*theta-y)/(2*m)



def bgdLR(rate, maxLoop, epsilon, X, y):
    '''
    bgd = batch gradient descent
    
    Args:
        rate: study rate
        maxLoop
        epsilon: convergence accuracy
        X
        y
        
    Returns:
        theta, errors, thetas, timeConsumed
    '''
    m,n = X.shape
    theta = np.zeros((n,1))
    count = 0
    converged = False
    error = float('inf')
    errors = []
    thetas = {}
    while count <= maxLoop:
        if (converged):
            break
        count = count + 1
        deriv = (1/m)*(y-X*theta).T*X[j] #
        for j in range(n):
            theta[j,0] = theta[j,0] + rate*deriv #有疑问
            thetas[j].append(theta[j,0])
        error = J(theta, X, y)
        errors.append(error)
        if (error < epsilon):
            converged = True
    return theta, errors, thetas
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        