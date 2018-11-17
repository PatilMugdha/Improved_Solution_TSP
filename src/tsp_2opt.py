
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
import pandas as pd
import time
import math
import random
import matplotlib.pyplot as plot

#loadData 
def readFile(filename):
    with open(filename) as citiesData:
        content = citiesData.read()
    return content


# In[2]:
# =============================================================================
# load file and parse it
# =============================================================================
def parseFile(content):
    lines = content.split('\n')
    #print(lines)
    cities = []
    reading=False
    totalRecords=0
    for line in lines:
        if 'EOF' in line:
            reading=False
            if len(cities)!=totalRecords:
                print('Error loading file')
                exit(0)
        if 'DIMENSION' in line:
            totalRecords=int(line.split(":")[1])
        if 'NODE_COORD_SECTION' in line:
            reading=True
            continue
        if reading:
            tokens = line.split(" ") 
            x = float(tokens[1])
            y = float(tokens[2])
            city = (x,y)
            cities.append(city)
    return cities


# In[3]:

# =============================================================================
#  Find Euclidean Distance 
# =============================================================================
def findDistance(prevCity, currentCity):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(prevCity, currentCity)]))


# =============================================================================
# Find the tour length    
# =============================================================================
def tourLength(cities):
    prevCity = cities[len(cities) - 1];
    distance = 0
    
    for currentCity in cities:
        distance += findDistance(prevCity, currentCity)
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
                if (findDistance(cities[i],cities[i-1])+findDistance(cities[j+1],cities[j]))>=(findDistance(cities[i],cities[j+1])+findDistance(cities[i-1],cities[j])):
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

# =============================================================================
# Plot the path taken by 2-opt algorithm    
# =============================================================================
def framec( solution, nc ):
    saveme = 1
    cities = np.array( solution )
    plot.axis( [-100,1700,-100,1200] )
    plot.plot(*zip(*cities))
    plot.title('{} Cities, 2-Opt Algorithm'.format(nc))
    plot.show()
    plot.savefig( ("%05d" % saveme)+'.png')
    plot.clf()

def plot_tsp(cities):
    plot.scatter(*zip(*cities))
    
# In[6]:


def main():
    
    print("Solution to Traveling Salesman Problem by 2-opt technique")
    content = readFile(path.relpath('data/randomTsp100.tsp'))
    cities = parseFile(content)
    length = tourLength(cities)
    print(f'Initial length: {length}')
    result = twoOpt(cities)
    length = tourLength(result)
    print(f'Distance found by 2-opt method: {length}')
    framec(result,100)


if __name__ == '__main__':
    main()

