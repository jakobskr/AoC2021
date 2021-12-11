def printOcts (octopods):
    for row in octopods:
        s = ""
        for oct in row:
            s += str(oct)
        print(s)
    print()

def flash(x,y):
    for i,j in neigh(x,y):
        octopods[i][j] += 1
        if octopods[i][j] > 9 and (i,j) not in flashed:
            flashed.append((i,j))
            flash(i,j)

octopods = []
validNeighbours = {}
for line in open("day11_input","r"):
    octopods.append([int(x) for x in line.strip()])

h = len(octopods)
w = len(octopods[0])

flashed = []

neigh = lambda x, y: {(max(x - 1, 0), y), (max(x - 1, 0), max(y - 1, 0)), (max(x - 1, 0), min(y + 1, w - 1)),
(x, max(y - 1, 0)), (x, min(y + 1, w - 1)), (min(x + 1, h - 1), y), (min(x + 1, h - 1), max(y - 1, 0)), (min(x + 1, h - 1), min(y + 1, w - 1))}

print(neigh(5,5))
flashes = 0
printOcts(octopods)
for day in range(0,1000):
    flashed = []

    for x in range(len(octopods)):
        for y in range(len(octopods[0])):
            octopods[x][y] += 1

            if octopods[x][y] > 9 and (x,y) not in flashed:
                flashed.append((x,y))
                flash(x,y)
                

    for x in range(len(octopods)):
        for y in range(len(octopods[x])):
            if octopods[x][y] > 9: 
                flashes += 1
                octopods[x][y] = 0
    
    
    if sum(list(map(sum, octopods))) == 0:
        print("all flashed at step {}".format(day + 1))
        break
    print("after {} steps:".format(day + 1))
    printOcts(octopods)

print(flashes)