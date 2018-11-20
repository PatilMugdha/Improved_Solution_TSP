
# coding: utf-8

# In[30]:


# In[1]:

"""
Created on Thu Nov 18, 18:30:17 2018

@author: PatilMugdha
"""

# =============================================================================
#  load libraries
# =============================================================================
import decimal
import math
import sys
import decimal
import math
import sys
from os import path
import numpy as np
import time
import math
import random
import matplotlib.pyplot as plot
from tsp_helper import loadFile, plotGraph, getDistance, plot_tsp
from tsp_greedy import greedy
from tsp_2opt import two_opt_swap,twoOpt,tourLength


def main():
    
    print("Solution to Traveling Salesman Problem by Greedy and 2-opt techniques")
    cities = loadFile('../data/randomTsp100.tsp')
    length = tourLength(cities)
    plotGraph(cities,100,'Initial graph')
    print(f'Initial length: {length}')

    #Greedy Algorithm result calculated before 2-opt technique
    pathLength, nearestNeighbors = greedy(cities)
    print(f'Distance found by Greedy method: {pathLength}')
    plotGraph(nearestNeighbors,100,'Greedy')
    
    #Output of greedy result given to 2-opt
    result = twoOpt(nearestNeighbors)
    length = tourLength(result)
    print(f'Distance found by 2-opt method: {length}')
    plotGraph(result,100,'2-opt')


if __name__ == '__main__':
    main()

