def match(pattern, number):
    if set(pattern).issubset(number):
        return True
    return False

def matchLength(length, l):
    for x in l:
        if len(x) == length:
            return x
    print("oof")

def part1():
    lens = [2,3,4,7]
    sums = 0
    for line in open("day8_input", "r"):
        input, output = line.split(" | ")
        output = output.split()
        sums += sum(list(map(lambda x : 1 if len(x) in lens else 0,  output)))
    print(sums)

def part2():
    sum = 0
    for line in open("day8_input", "r"):
        input, output = line.split(" | ")
        input = [list(x) for x in input.split()]
        input.sort(key = lambda x: len(x))
        dikt = {"0":[], "1":matchLength(2,input), "2":[], "3":[], "4":matchLength(4, input), 
        "5":[], "6":[], "7":matchLength(3,input), "8":matchLength(7,input), "9":[]}
        top = list(set(dikt["1"]) ^ set(input[1]))[0]

        for x in input:
            if len(x) != 5: continue
            if match(dikt["1"], x):
                dikt["3"] = x
                #print(dikt["3"])
                break

        middle = list(((set(dikt["3"]) & set(dikt["4"]) ^ set(dikt["1"]) )))
        topLeft = list(set(dikt["4"]) ^ set(dikt["1"]) ^ set(middle))
        dikt["0"] = list(set(dikt["8"]) ^ set(middle))
        dikt["9"] = dikt["3"] + topLeft
        
        for x in input:
            if len(x) == 6:
                if not match(dikt["1"], x):
                    dikt["6"] = x
        
        topRight = list(set(dikt["6"]) ^ set(dikt["8"]))
        bottomRight = list(set(topRight) ^ set(dikt["1"]))
        dikt["5"] = list(set(dikt["9"]) ^ set(topRight))
        dikt["2"] = list((set(dikt["8"]) ^ set(bottomRight)) ^ set(topLeft))

        num = ""
        for n in [list(x) for x in output.split()]:
            for ind, x in dikt.items():
                if set(x) == set(n):
                    num += ind

        print(output.split(), ":" ,num)
        sum += int(num)
    print("final sum:", sum)

part1()
part2()    