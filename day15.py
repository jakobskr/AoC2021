
from typing import Iterable
import numpy as np

def printArray(array):
    for row in array:
        rep = ""
        for x in row:
            rep += str(x) + " "
        print(rep)
    print(rep)

def shortDist(graph, distance):
    cord = graph[0]
    low = distance[cord[1]][cord[0]]

    for y,row in enumerate(distance):
        for x, val in enumerate(row):
            if (x,y) in graph:
                if val < low:
                    val = low
                    cord = (x,y)
    return cord
    

paths = []
cave = []
height, width = 0,0
validNeighbours = lambda x, y : {(max(x - 1, 0),y) , (min(x + 1, width), y), (x, max(y - 1, 0)), (x, min(y + 1, height))}


for line in open("day15_input","r"):
    row = []
    for l in line.strip():
        row.append(int(l))
    cave.append(row)
print (cave)

height = len(cave)
width = len(cave)

print(validNeighbours(3,3))
print("w:",width, "h",height)
# begin djikstra
distance = [[9999999 for x in range(width)] for y in range(height)]
graph = [(x,y) for x in range(width) for y in range(height)]
prev = [[0 for x in range(width)] for y in range(height)]
end = (width - 1, height - 1)
distance[0][0] = 0
print(graph)
print(shortDist(graph, distance))
pop = lambda : graph[distance.index(min(distance))]
print(pop())

while graph:
    u = shortDist(graph,distance)

    graph.remove(u)

    print(u)
    if u == end:
        print("found path")
        break
    
    for x,y in validNeighbours(*u,):
        if (x,y) in graph:
            alt = distance[u[1]][u[0]] + cave[y][x]
            if alt < distance[y][x]:
                distance[y][x] = alt
                prev[y][x] = u
printArray(distance)
printArray(prev)