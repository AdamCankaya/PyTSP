# Adam Cankaya, Ismail Orabi, Kevin Kozee
# CS 325 Project 5 Group 10
# References: 
    # http://nbviewer.ipython.org/url/norvig.com/ipython/TSPv3.ipynb
# Need to fix:
    # Correct input with additional white space in textfile?
    # Only works assuming city id number is the same as line number in text file
# Upgrade:
    # Try starting from other cities and picking best distance

import sys

# Finds distance between two cities in format [ID, x, y]
def pointDistance(a,b):
    x1 = a[1]
    y1 = a[2]
    x2 = b[1]
    y2 = b[2]
    pointDist = int(round(pow((pow((x2-x1),2) + pow((y2-y1),2)),0.5)))
    return pointDist

# Finds total distance along a tour of cities
def totalDistance(tour_list):
    dist = 0
    for i in range(0, len(tour_list)-1):
        dist = dist + pointDistance(tour_list[i], tour_list[i+1])
    return dist

# Greedy Approach: starting from first city find nearest neighbor and add to tour
def greedyTSP(cities):
    start = cities[0]
    tour = [start]
    unvisited = cities
    del cities[0]
    while unvisited:
        neighbor = closestNeighbor(tour[-1], unvisited)
        tour.append(neighbor)
        unvisited.remove(neighbor)
    
#    tour.append(start)  # return to starting city

    return tour

# Find the closest neighbor to startCity in a list of cities
def closestNeighbor(startCity, cities):
    neighbor = cities[0]
    bestI = 0
    bestDist = pointDistance(startCity, neighbor)
    for i in range(0,len(cities)):
        tempDist = pointDistance(startCity, cities[i])
        if tempDist > 0:
            if tempDist < bestDist:
                bestDist = tempDist
                bestI = i
    return cities[bestI]

# **** MAIN FUNCTION ****
cities = []     # [(city ID, x-cord, y-cord)]
tour = []       # order of cities in final tour

#open read and write files
file = sys.argv[1]
input = open(file, "r", 1)
fileOut = file + ".tour"
output = open(fileOut, "w", 1)

#read in all lines, split on spaces, remove new line
lines = input.readlines()
for line in lines:
	cities.append(line.lstrip().split())

#loop through cities and change values to int
for i in range(0,len(cities)):
    cities[i][0] = int(cities[i][0])
    cities[i][1] = int(cities[i][1])
    cities[i][2] = int(cities[i][2])

tour = greedyTSP(cities)

#write results to output file
distance = totalDistance(tour)
output.write(str(distance) + '\n')
for i in range(0,len(tour)):
    output.write(str(tour[i][0]) + '\n')