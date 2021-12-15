
from typing import Iterable
from collections import defaultdict
import numpy as np
import heapq as hq

def printArray(array):
    for row in array:
        rep = ""
        for x in row:
            rep += str(x) + " "
        print(rep)
    print()

def solve(tiles):
    largeCave = []
    paths = []
    cave = []
    height, width = 0,0
    
    for line in open("day15_input","r"):
        row = []
        for l in line.strip():
            row.append(int(l))
        cave.append(row)

    height = len(cave)
    width = len(cave[0])

    for y in range(height * tiles):
        row = []
        for x in range(width * tiles):
            val = cave[y % height][x % width] + x // width + y // height
            row.append((val - 1) % (9) + 1)
        largeCave.append(row)

    width *= tiles
    height *= tiles

    validNeighbours = lambda x, y : {(max(x - 1, 0),y) , (min(x + 1, width - 1), y), (x, max(y - 1, 0)), (x, min(y + 1, height - 1))}
    cave = largeCave
    # begin djikstra
    
    distance = [[9999999 for x in range(width)] for y in range(height)]
    graph = [(x,y) for x in range(width) for y in range(height)]
    end = (width - 1, height - 1)
    distance[0][0] = 0

    queue = []
    hq.heappush(queue,(0,(0,0)))
    visited = set()

    while graph:
        #print(queue)
        dist, node = hq.heappop(queue)

        if node == end:
            break

        if node in visited:
            continue

        visited.add(node)
        nx,ny = node

        for x,y in validNeighbours(*node):
            if (x,y) not in visited:
                alt = dist + cave[y][x]
                if alt < distance[y][x]:
                    distance[y][x] = alt
                    hq.heappush(queue, (alt, (x,y)))

    print(distance[-1][-1])


solve(1)
solve(5)