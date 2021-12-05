
def newRange(x,y):
    if x < y:
        return range(x,y)
    else: 
        tmp = list(range(y - 1,x + 1)); tmp.reverse()
        return tmp

cordinates = {}

for line in open("day5_input"):
    cords = line.strip().split(" -> ")
    x1,y1 = [int(y) for y in cords[0].split(",")]
    x2, y2 = [int(y) for y in cords[1].split(",")]

    if x1 == x2:
        for i in newRange(y1,y2 + 1):
            if "({},{})".format(i, x1) in cordinates:
                cordinates["({},{})".format(i,x1)] += 1
            else:
                cordinates["({},{})".format(i,x1)] = 1
    elif y1 == y2:
        for i in newRange(x1,x2 + 1):
            if "({},{})".format(y1,i) in cordinates:
                cordinates["({},{})".format(y1,i)] += 1
            else:
                cordinates["({},{})".format(y1,i)] = 1
    else:
        print(x1, ":", y1 , "->" , x2, ":", y2)
        cords = zip(newRange(x1,x2 + 1), newRange(y1, y2 + 1))
        print(list(newRange(x1,x2 + 1)), list(newRange(y1, y2 + 1)))
        for cord in cords:
            #print(cord)
            if "({},{})".format(cord[1], cord[0]) in cordinates:
                cordinates["({},{})".format(cord[1], cord[0])] += 1
            else:
                cordinates["({},{})".format(cord[1], cord[0])] = 1

num = len([x for x in cordinates.values() if x > 1])

print("amount of intersections: ", num)