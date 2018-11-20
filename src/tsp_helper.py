#This file contains the helper methods such as plot the graphs, parsing file and finding the distances.
"""
Created on Fri Nov 17 21:15:57 2018

@author: aparnakale
"""
import numpy as np
import math
import matplotlib.pyplot as plot

#
# =============================================================================
# Plot the path taken by greedy algorithm
# =============================================================================
def plotGraph( solution, nc,title):
    saveme = title
    cities = np.array(solution)
    plot.axis( [-100,1700,-100,1200] )
    plot.plot(*zip(*cities))
    plot.title('{} Cities, {}'.format(nc,title))
    plot.show()
    plot.savefig((saveme)+'.png')
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
