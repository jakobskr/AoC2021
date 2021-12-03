def part1():
    previous = 0 
    cur = 0
    count = 0
    f =  open("day1_input","r")
    previous = int(f.readline())
    for line in f:
        if(int(line) > previous):

            #print(line)
            count = count + 1
        previous = int(line)
    return count

def part2():
    f = open("day1_input", "r")
    l = [int(x) for x in f.read().split("\n")]
    triples = [sum(l[s: s + 3]) for s in range(0, len(l) - 2)]
    #print(triples)
    count = 0
    prev = l[0]
    for cur in triples[1:]:
        if cur > prev:
            count += 1
        prev = cur
    return count

print("part1:", part1())
print("part2:", part2())