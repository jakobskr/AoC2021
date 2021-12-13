

def printDots():
    maxX = max([x[0] for x in dots])
    maxY = max([x[1] for x in dots])


    for y in range(0, maxY + 1):
        str = ""
        for x in range(0, maxX + 1):
            if (x,y) in dots:
                str += "#"
            else:
                str += "."
        print(str)
    print()


inst = []
dots = []
maxX = 0
maxY = 0
for line in open("day13_input"):
    print(len(line))
    if len(line) < 2:
        continue
    
    if line.startswith("fold"):
        print(line[11:].strip().split("="))
        
        inst.append(line[11:].strip().split("="))
        continue
    
    x,y = [int(x) for x in line.strip().split(",")]
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y

    dots.append((x,y))

print(dots)
print(inst)
print("len dots before:", len(dots))
#printDots()

for fold, i in inst:
    i = int(i)
    newDot = []
    for x,y in dots:
        #print(fold, i ,":" ,x,y)
        if fold == "y":
            if y == i:
                continue
            elif y < i and (x,y) not in newDot:
                newDot.append((x,y))
            elif y > i and (x, 2*i - y) not in newDot:
                newDot.append((x, 2*i - y))
        
        if fold == "x":
            if x == i:
                continue
            elif x < i and (x,y) not in newDot:
                newDot.append((x,y))
            elif x > i and (2*i - x, y) not in newDot:
                newDot.append((2*i - x, y))

    dots = newDot[:]
    
    print(len(dots))
    ##print(dots)
    #printDots()

print(dots)
print(len(dots))

printDots()