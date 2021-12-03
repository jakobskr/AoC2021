bins = []
length = 12

def part1():
    counter = [0] * length
    c = 0
    for line in open("day3_input", "r"):
        binaryL = int(line,base=2)
        c += 1
        #print(line.strip())
        for i in range(0,length):
            counter[length - 1 - i] += (binaryL & (1 << i)) >> (i)
            #print((binaryL & (1 << i)) >> i, (binaryL & (1 << i)))
            #print(binaryL & 1 << i)
        bins.append( int(line, base=2))
    print(counter, c)

    gamma = ""
    epsilon =""
    for i in counter:
        if i < c / 2:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print(int(gamma, base=2) * int(epsilon, base=2),gamma, epsilon)
    return counter, gamma, epsilon

def part2(counter, gamma, epsilon):
    oxyPort = bins[:]
    #print(oxyPort)
    i = length - 1
    for i in range(0,length):
        oxyLen = len(oxyPort)
        if(len(oxyPort) == 1):
            print("last value found")
            break
        
        shiftRate = length - 1 - i
        tempList = []
        c = 0
        for numb in oxyPort:
            c += (numb & (1 << shiftRate)) >> (shiftRate)

        for numb in oxyPort:
            if c >= oxyLen / 2: #keep 1s
                if (numb & (1 << shiftRate)):
                    tempList.append(numb)
            else:
                if not (numb & (1 << shiftRate)):
                    tempList.append(numb)

        oxyPort = tempList[:]

    print("oxyVAL = {:05b}".format(oxyPort[0]))

    carPort = bins[:]
    #print(carPort)
    i = length - 1
    for i in range(0,length):
        carLen = len(carPort)
        if(len(carPort) == 1):
            print("last value found")
            break
        
        shiftRate = length - 1 - i
        tempList = []
        c = 0
        for numb in carPort:
            c += (numb & (1 << shiftRate)) >> (shiftRate)

        for numb in carPort:
            if c >= carLen / 2: #keep 1s
                if not (numb & (1 << shiftRate)):
                    tempList.append(numb)
            else:
                if (numb & (1 << shiftRate)):
                    tempList.append(numb)

        carPort = tempList[:]
        print("after ", i , " bit:", tempList, c)
    print("carVAL = {:05b}".format(carPort[0]))

    print("ANS = oxy * car:", oxyPort[0] ,"*",  carPort[0], "=", oxyPort[0] * carPort[0])

counter, gamma, epsilon, = part1()
part2(counter, gamma, epsilon)