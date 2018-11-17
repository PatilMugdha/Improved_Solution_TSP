
# coding: utf-8

# In[27]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 21:15:57 2018

@author: aparnakale
"""
# =============================================================================
#  load libraries
# =============================================================================
import numpy as np
import pandas as pd
import time
import math
import random
import matplotlib.pyplot as plot


# =============================================================================
# Plot the path taken by greedy algorithm    
# =============================================================================
def framec( solution, nc ):
    saveme = 0
    cities = np.array( solution )
    plot.axis( [-100,1700,-100,1200] )
    plot.plot(*zip(*cities))
    plot.title('{} Cities, Greedy Algorithm'.format(nc))
    plot.show()
    plot.savefig( ("%05d" % saveme)+'.png')
    plot.clf()

    
# =============================================================================
# load file and parse it
# =============================================================================
def loadFile(filename):
    cities = []
    with open(filename) as f:
        lines = f.readlines()
        start_to_read = False
        for line in lines:
            if 'DIMENSION' in line:
                n_cities = line.split(':')[1]
                continue
            if 'EOF' in line:
                break
            if 'NODE_COORD_SECTION' in line:
                start_to_read = True
                continue
            if start_to_read:
                x = line.split(' ')[1]
                y = line.split(' ')[2]
                cities.append((float(x),float(y)))
        return cities

    
# =============================================================================
#  Show all the cities    
# =============================================================================
def plot_tsp(cities):
    plot.scatter(*zip(*cities))

    
# =============================================================================
#  Find Euclidean Distance 
# =============================================================================
def getDistance(currentCity, nextCity):
    return math.sqrt(np.square(currentCity[0] - nextCity[0]) + np.square(currentCity[1]-nextCity[1]))  

  
# =============================================================================
# Traveling Salesman using greedy approach     
# =============================================================================
def greedy(cities):
    visited = []        # Initialize
    routeDistance = 0
    mustVisit = cities  # Select a city randomly and set it as home city
    home = random.choice(cities)
    visited.append(home)# Maintains the list of cities visited so far
    cities.remove(home)
    currentCity = home
    nearCity = currentCity
    while currentCity:
        shortest = float('inf')  #set distance to infinity
        for someCity in mustVisit:
                someDistance = getDistance(currentCity,someCity)
                if(someDistance<shortest):
                    shortest = someDistance
                    nearCity = someCity
        if(shortest == float('inf')):
            break
        mustVisit.remove(nearCity)        
        visited.append(nearCity)
        currentCity = nearCity
        routeDistance = shortest + routeDistance
    routeDistance = routeDistance + getDistance(nearCity,home)
    plot_tsp(visited)
    visited.append(home)
    return routeDistance, visited
        
def main():
    cities = loadFile('../data/randomTsp100.tsp')
    tsp_path, all = greedy(cities)
    print('----Traveling Salesman Problem by Greedy Method----')
    print('Total distance travelled by Salesman')
    print(tsp_path)
    framec(all,100)

if __name__ == '__main__':
    main()

