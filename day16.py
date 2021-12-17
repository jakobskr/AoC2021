from functools import reduce

def parseLit(bitstring, i):
    print(bitstring[i:])
    startI = i
    version = int(bitstring[i:i +3], base=2)
    type = bitstring[i + 3: i + 6]
    i += 6
    val = ""
    while(True):
        if bitstring[i] == "1":
            val += bitstring[i + 1 : i + 5]
            i += 5
        else:
            val += bitstring[i + 1: i + 5]
            i += 5
            break 
    return version, type, val, i - startI

def parseOp(bitstring, i):
    startI = i

    version = int(bitstring[i:i + 3],base=2)
    type = typeCheck(i)
    i += 6

    lflag = bitstring[i] ; i += 1
    versionSum = version

    if lflag == "1":
        #number of subpackets
        l = int(bitstring[i : i + 11], base=2)
        i += 11
        print(l, "subpackets")
        read = 0
        vals = []
        while read < l:
            if typeCheck(i) == "100":
                version, _, val, packLen = parseLit(bitstring, i)
                versionSum += version
                vals.append(int(val, base=2))
                i += packLen
            else:
                version, _, val, packLen = parseOp(bitstring,i)
                versionSum += version
                vals.append(val)
                i += packLen
            read += 1
        print("here", vals) 
        #rturn versionSum, type, vals, i - startI
        
    else:
        #length of subpacktes
        l = int(bitstring[i : i + 15], base=2)
        i += 15
        print(l)

        read = 0
        vals = []
        while read < l:
            if typeCheck(i) == "100":
                version, _, val, packLen = parseLit(bitstring, i)
                versionSum += version
                read += packLen
                i += packLen
                vals.append(int(val, base=2))
            else:
                version, _, val, packLen = parseOp(bitstring,i)
                versionSum += version    
                vals.append(val)
                read += packLen
                i += packLen
        #return versionSum, type, vals, i - startI

    if type == "000":
        ret = sum(vals)

    elif type == "001":
        ret = 1
        for x in vals:
            ret *= x
    elif type == "010":
        ret = min(vals)
    elif type == "011":
        ret = max(vals)
    elif type == "101":
        ret = 1 if vals[0] > vals[1] else 0
    elif type == "110":
        ret = 1 if vals[0] < vals[1] else 0
    elif type == "111":
        ret = 1 if vals[0] == vals[1] else 0

    print("subot ret",ret)
    return versionSum, type, ret, i - startI



hexa = {"0" : "0000", "1" : "0001","2" : "0010",
"3" : "0011","4" : "0100","5" : "0101","6" : "0110",
"7" : "0111","8" : "1000","9" : "1001","A" : "1010",
"B" : "1011",
"C" : "1100",
"D" : "1101",
"E" : "1110",
"F": "1111"}

bitstring = ""
for x in open("day16_input", "r").read().strip():
    bitstring += hexa[x]

print(bitstring)

typeCheck = lambda x: bitstring[x + 3: x + 6]

i = 0
versionSum = 0
while i < len(bitstring):
    print(bitstring[i:])
    startI = i
    versionSum += int(bitstring[i:i + 3], base=2)
    type = bitstring[3: 3 + i + 3]
    i += 6

    if type == "100":
        #literal value
        val = ""
        while(True):
            if bitstring[i] == "1":
                val += bitstring[i + 1 : i + 5]
                i += 5
            else:
                val += bitstring[i + 1: i + 5]
                i += 5
                break   
        print(val, int(val, base=2))


        print(type)
    else:
        #operator expand part 2 most likely : )
        lflag = bitstring[i] ; i += 1
        
        if lflag == "1":
            #number of subpackets
            l = int(bitstring[i : i + 11], base=2)
            i += 11
            print(l, "subpackets")
            read = 0
            vals = []
            while read < l:
                if typeCheck(i) == "100":
                    version, _, val, packLen = parseLit(bitstring, i)
                    versionSum += version
                    vals.append(int(val, base=2))
                    i += packLen
                else:
                    version, _, val, packLen = parseOp(bitstring,i)
                    versionSum += version
                    vals.append(val)
                    i += packLen
                read += 1
            print(vals)
            
        else:
            #length of subpacktes
            l = int(bitstring[i : i + 15], base=2)
            i += 15
            print(l)

            read = 0
            vals = []
            while read < l:
                if typeCheck(i) == "100":
                    version, _, val, packLen = parseLit(bitstring, i)
                    versionSum += version
                    read += packLen
                    i += packLen
                    vals.append(int(val, base=2))
                else:
                    print("subOperator hell : )")
                    version, _, val, packLen = parseOp(bitstring,i)
                    versionSum += version
                    vals.append(val)
                    read += packLen
                    i += packLen
            print(vals)
        
        ret = "noOP"
        print("type",type)
        if type == "000":
            ret = sum(vals)

        elif type == "001":
            ret = 1
            for x in vals:
                ret * ret
        elif type == "010":
            ret = min(vals)
        elif type == "011":
            ret = max(vals)
        elif type == "101":
            ret = 1 if vals[0] > vals[1] else 0
        elif type == "110":
            ret = 1 if vals[0] < vals[1] else 0
        elif type == "111":
            ret = 1 if vals[0] == vals[1] else 0

        print(versionSum, type, ret, i - startI)
            
    break
            
    

print(versionSum)

    
     