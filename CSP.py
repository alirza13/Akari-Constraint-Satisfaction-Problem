# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 23:36:12 2018

@author: ALIRZA GULIYEV 20026
"""
from constraint import *

'''
graph = [ ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X'],   # 7X7 hw2
          ['Y', 'Y', '4', 'Y', 'Y', 'Y', 'Y'],
          ['0', 'Y', 'Y', 'Y', '1', 'X', 'Y'],
          ['Y', 'Y', 'Y', '1', 'Y', 'Y', 'Y'],
          ['Y', 'X', '1', 'Y', 'Y', 'Y', 'X'],
          ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y'],
          ['1', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']
        ]
'''

graph = [ ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y'],  # 7X7 Hard 
          ['Y', '2', 'Y', 'Y', 'Y', '0', 'Y'],
          ['1', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
          ['Y', 'Y', 'Y', '2', 'Y', 'Y', 'Y'],
          ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', '2'],
          ['Y', '2', 'Y', 'Y', 'Y', '3', 'Y'],
          ['Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y']
        ]

'''
graph = [ ['Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X'],  # 7X7 
          ['Y', '4', 'Y', 'Y', '1', 'Y', 'X'],
          ['Y', 'Y', 'Y', '2', 'Y', 'Y', 'Y'],
          ['Y', 'X', 'Y', 'Y', 'Y', 'X', 'Y'],
          ['Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y'],
          ['X', 'Y', 'X', 'Y', 'Y', '1', 'Y'],
          ['1', 'Y', 'Y', 'Y', '1', 'Y', 'Y']
        ]
'''

'''
graph = [ ['Y', 'Y', '1', 'Y', '2', 'Y', 'Y'],  # 7X7 Normal 
          ['Y', 'Y', 'Y', '2', 'Y', 'Y', 'Y'],
          ['2', 'Y', 'Y', 'Y', 'Y', 'Y', 'X'],
          ['Y', 'X', 'Y', 'Y', 'Y', 'X', 'Y'],
          ['1', 'Y', 'Y', 'Y', 'Y', 'Y', '3'],
          ['Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y'],
          ['Y', 'Y', '2', 'Y', 'X', 'Y', 'Y']
        ]   
'''

'''
graph = [ ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y','Y','Y','Y'],  # 10X10 Hard 
          ['Y', 'X', '0', 'Y', 'Y', '1', 'Y','Y','1','Y'],
          ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y','Y','1','Y'],
          ['Y', 'Y', 'Y', 'X', '1', 'Y', '0','Y','Y','Y'],
          ['Y', '4', 'Y', 'Y', 'Y', 'Y', '0','Y','Y','Y'],
          ['Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y','Y','X','Y'],
          ['Y', 'Y', 'Y', 'X', 'Y', 'X', '0','Y','Y','Y'],
          ['Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y','Y','Y','Y'],
          ['Y', '0', 'Y', 'Y', '1', 'Y', 'Y','2','0','Y'],
          ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y','Y','Y','Y']
        ] 
'''

def whichSectionX (x,y):
    left = y
    right = y
    sector = []
    while left >= 0 and graph[x][left] == 'Y':
        left = left - 1
    left = left + 1    
    while right < len(graph) and graph[x][right] == 'Y':
        right = right + 1
    right = right - 1
    sector.append([x,left])
    sector.append([x,right])
    return sector

def whichSectionY (x,y):
    up = x
    down = x
    sector = []
    while up >= 0 and graph[up][y] == 'Y':
        up = up - 1
    up = up + 1
    while down < len(graph[0]) and graph[down][y] == 'Y':
        down = down + 1
    down = down - 1
    sector.append([up,y])
    sector.append([down,y])
    return sector
    
def blackInBetweenX (x):   # Check for sector in rows 
    sectors = []
    startingPos = 0
    y = 0
    while y < len(graph[0]):
        if graph[x][y] != 'Y':
            startingPos = startingPos + 1
            y = y + 1
        else: 
            break
    while y < len(graph[0]):
        if graph[x][y] != 'Y':
            sectors.append([startingPos,y - 1])
            if y + 1 < len (graph[0]) and  graph[x][y + 1] == 'Y':
                startingPos = y + 1
                y = y + 1
            else:
                while y < len(graph[0]) and graph [x][y] != 'Y':
                    y = y + 1
                startingPos = y
        
        elif (y == len(graph[0]) - 1 and graph [x][y] == 'Y'):
                sectors.append([startingPos,y])
                break
        else:
            y = y + 1
    return sectors           

def blackInBetweenY (y):       # Check for sector in columns 
    sectors = []
    startingPos = 0
    x = 0
    while x < len(graph):
        if graph[x][y] != 'Y':
            startingPos = startingPos + 1
            x = x + 1
        else:
            break
        
    while x < len(graph):      
        if graph[x][y] != 'Y':
            sectors.append([startingPos,x - 1])
            if x + 1 < len(graph) and graph[x + 1][y] == 'Y':
                startingPos = x + 1
                x = x + 1
            else:
                while x < len(graph) and graph[x][y] != 'Y':
                    x = x + 1
                startingPos = x
        elif x == len (graph) - 1 and graph[x][y] == 'Y':
            sectors.append([startingPos,x])
            break
        else:
            x = x + 1
    return sectors

     
print(blackInBetweenY(6))   
problem = Problem(BacktrackingSolver())

for x in range(len(graph)):        # variable creation
    for y in range (len(graph[0])):
        if graph[x][y] == 'Y':
            variable = (x,y)
            problem.addVariable(variable,[0,1])
 
        
for x in range(len(graph)):        # there can be at most 1 bulb in every row section
    for sector in blackInBetweenX(x):
        start = sector[0]
        end = sector[1]
        problem.addConstraint(MaxSumConstraint(1),[(x,z)  for z in range (start,end + 1) if graph[x][z] == 'Y'])

        
for y in range (len(graph[0])):   # there can be at most 1 bulb in every column section
    for sector in blackInBetweenY(y):
        start = sector[0]
        end = sector[1]
        problem.addConstraint(MaxSumConstraint(1),[(z,y)  for z in range (start,end + 1 ) if graph[z][y] == 'Y'])


for x in range(len(graph)):     # checking for how many bulbs can be put next to numbers
    for y in range(len(graph[0])):
        if graph[x][y].isdigit():
            constraintNumber = int(graph[x][y])
            problem.addConstraint(ExactSumConstraint(constraintNumber),[(x + i,y + j) for i,j in zip([-1,1,0,0], [0,0,-1,1]) if x + i >= 0 and x + i < len(graph) and y + j < len (graph[0]) and y + j >= 0 and graph[x + i][y + j] == 'Y' ])
         
            
for x in range (len(graph)):    # checking for every cell and making sure row and column sections that contains this cell have minimum one bulb 
    for y in range (len(graph[0])):
        if graph[x][y] == 'Y':
            sectorRow = whichSectionX(x,y)
            sectorColumn = whichSectionY(x,y)
            sectorRowStart = sectorRow[0]
            sectorRowEnd = sectorRow[1]
            sectorColumnStart = sectorColumn[0]
            sectorColumnEnd = sectorColumn[1]
            xArray = []
            yArray = []
            xIterator = sectorRowEnd[1] - sectorRowStart[1] + 1
            for i in range(xIterator):
                xArray.append(x)
            for i in range (sectorRowStart[1],sectorRowEnd[1] + 1):
                yArray.append(i)
            
            yIterator = sectorColumnEnd[0] - sectorColumnStart[0] + 1
            for i in range(yIterator):
                yArray.append(y)
            for i in range (sectorColumnStart[0],sectorColumnEnd[0] + 1):
                xArray.append(i)
            problem.addConstraint(MinSumConstraint(1),[(x,y) for x,y in zip(xArray,yArray)])            


solutions = problem.getSolution()

for key,value in solutions.items():
    if (value == 1):
        print(key)









