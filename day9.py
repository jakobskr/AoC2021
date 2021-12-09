
def printMap(vis):

    for row in vis:
        string = ""
        for val in row:
            if val: string += "t" 
            else: string += "f"
        print(string)
    print()


grid = []
for line in open("day9_input", "r"):
    #print(line)
    row = []
    for l in line.strip():
        row.append(int(l))
    grid.append(row)

iMax = len(grid)
jMax = len(grid[0])

print(iMax, jMax)
print(grid)
sum = 0
for i, row in enumerate(grid):
    #print(row)
    for j, cell in enumerate(row):
        if (not i - 1 == -1) and grid[i - 1][j] <= cell:
            continue
        if (not i + 1 == iMax) and grid[i + 1][j] <= cell:
            continue
        if (not j - 1 == -1) and grid[i][j - 1] <= cell:
            continue
        if (not j + 1 == jMax) and grid[i][j + 1] <= cell:
            continue
        #print("low point", cell, i, j)
        sum += 1 + cell
print("sum of Low Points", sum)
visitMap = []

def exploreBasin(i,j, grid):
    if(visitMap[i][j] == True):
        return []
    
    if(grid[i][j] == 9):
        visitMap[i][j] = True

        return []
    basin = []
    basin.append(grid[i][j])
    visitMap[i][j] = True

    if i - 1 >= 0:
        basin += exploreBasin(i - 1, j,  grid)
    if i + 1 < iMax:
        basin += exploreBasin(i + 1, j,  grid)
    if j - 1 >= 0:
        basin += exploreBasin(i, j - 1,  grid)
    if j + 1 < jMax:
        basin += exploreBasin(i, j + 1,  grid)
    
    return basin


basins = []
print(grid)

for i in range(0, iMax):
    visitMap.append([False] * jMax) 
x = 0
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if(visitMap[i][j]):
            continue
        if(cell == 9):
            visitMap[i][j] = True
            continue

    
        basin = []
        basin = exploreBasin(i,j, grid)
        basins.append(basin)

basins.sort(reverse=True, key=len)
score = 1
for i in range(0,3):
    score *= len(basins[i])
print(basins, "score:", score)


#print(visitMap)