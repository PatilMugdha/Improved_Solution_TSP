
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
import time
import math
import random
import matplotlib.pyplot as plot
from tsp_helper import plotGraph,loadFile,plot_tsp,getDistance

# =============================================================================
# Traveling Salesman using greedy approach     
# =============================================================================
def greedy(cities):
    visited = []        # Initialize
    routeDistance = 0
    mustVisit = cities  # Select a city randomly and set it as home city
    home = cities[0]
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
    plotGraph(all,100)

if __name__ == '__main__':
    main()

