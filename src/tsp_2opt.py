
# coding: utf-8

# In[1]:

"""
Created on Thu Nov 15, 11:55:17 2018

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
from tsp_helper import getDistance,loadFile,plot_tsp,plotGraph

# =============================================================================
# Find the tour length    
# =============================================================================
def tourLength(cities):
    prevCity = cities[len(cities) - 1];
    distance = 0
    
    for currentCity in cities:
        distance += getDistance(prevCity, currentCity)
        prevCity=currentCity
    return distance


# In[4]:

# =============================================================================
# Swap cross-edges     
# =============================================================================
def two_opt_swap(cities, i, j):
    newTour = []
    size = len(cities)
    for idx in range(0,i):
        newTour.append(cities[idx]) #append nodes before swap
    
    reverse=0
    for idx in range(i,j+1):
        newTour.append(cities[j-reverse])  #append in reverse order
        reverse+=1
        
    for idx in range(j+1,size):
        newTour.append(cities[idx]) #append nodes after swap
        
    return newTour


# In[5]:

# =============================================================================
# Travelling Salesman using 2-opt approach     
# =============================================================================
def twoOpt(cities):
    newTour = []
    bestDist = tourLength(cities)
    newDist = 0
    swaps = 1
    swapCount = 0
    
    while swaps!=0:
        swaps = 0
        for i in range(1,len(cities)-2):
            for j in range(i+1,len(cities)-1):
                if (getDistance(cities[i],cities[i-1])+getDistance(cities[j+1],cities[j]))>=(getDistance(cities[i],cities[j+1])+getDistance(cities[i-1],cities[j])):
                        newTour = two_opt_swap(cities, i, j)
                        newDist = tourLength(newTour) 
                        if (newDist < bestDist):
                            cities = newTour;
                            bestDist = newDist;
                            swaps+=1;
                            swapCount+=1;
    
    print(f'Total 2-opt swaps: {swapCount}')
    plot_tsp(cities)
    return cities


def main():
    
    print("Solution to Traveling Salesman Problem by 2-opt technique")
    cities = loadFile('../data/randomTsp100.tsp')
    length = tourLength(cities)
    print(f'Initial length: {length}')
    result = twoOpt(cities)
    length = tourLength(result)
    print(f'Distance found by 2-opt method: {length}')
    plotGraph(result,100)


if __name__ == '__main__':
    main()

