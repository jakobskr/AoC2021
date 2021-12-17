

def step(xVel,yVel):
    x = 0
    y = 0
    maxY = 0
    global totalIters
    #print("launch with:", xVel ,"x vel", yVel ,"y vel")
    while x <= xHigh and y >= yLow:
        #print(x , y)

        x += xVel
        y += yVel

        if y > maxY:
            maxY = y

        if xVel < 0: xVel += 1
        elif xVel > 0: xVel -= 1
        yVel -= 1


        if y == 0 and yVel < yLow:
            return False, 0

        

        if x >= xLow and x <= xHigh and y >= yLow and y <= yHigh:
            #print("happens")
            return True, maxY
        
        totalIters += 1
    return False, 0
        



x,y = open("day17_input","r").readline().strip().split(":")[1].split(", ")

print(x,y)
totalIters = 0

xLow, xHigh =  [int(i) for i in x.split("=")[1].split("..")]
yLow, yHigh = [int(i) for i in y.split("=")[1].split("..")]

print(xLow, "..", xHigh)
print(yLow, "..", yHigh)

max = 0
cords = 0


validShot = []
for i in range(-200,300):
    for j in range(-200,xHigh + 1):
        found, height = step(j,i)
        if found:
            validShot.append((j,i))
            if height > max:
                max = height
                cords = (j,i)

print("max height", max, cords)
print("valid shots: " , len(validShot))
#print(validShot)
print(totalIters)
print(step(6,9))

