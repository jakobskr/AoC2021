
from collections import defaultdict
import copy
rules = dict()


f = open("day14_input","r")
poly = f.readline().strip()
f.readline()
oldPoly = poly
for line in f:
    pair, rule = line.strip().split(" -> ")
    rules[pair] = rule

#print(poly,rules)
#print(list(rules.keys()))

for step in range(0,10):
    newPoly = ""
    for i in range(0,len(poly)):
        pair = poly[i:i+2]
        #print(pair, rules[pair])
        if pair in rules.keys():
            newPoly += pair[0] + rules[pair]
        else:
            newPoly += pair[0]
    poly = newPoly[:]
    #print("after step {}".format(step + 1), len(poly))

#print(set(poly))
result = list(map(lambda x : (x, len(list(filter (lambda y: x == y , poly)))), set(poly)))
result.sort(key=(lambda x: x[1]) )
print("part1:", result[-1][1] - result[0][1], result)


def part2():
    pairs = defaultdict(int)

    for i in range(0,len(oldPoly)):
        pair = oldPoly[i:i+2]
        #print(pair)
        pairs[pair] += 1

    for step in range(0, 40):

        newPairs = defaultdict(int)
        for pair, amount in pairs.items():
            #print(pair, amount)
            if pair in rules:
                newPairs[pair[0]+rules[pair]] += amount
                newPairs[rules[pair] + pair[1]] += amount
            else:
                newPairs[pair] += amount
        
        pairs = copy.deepcopy(newPairs)
        #print("after step {}:".format(step + 1), dict(newPairs))
    
    letters = defaultdict(int)

    for pair, amount in pairs.items():
        letters[pair[0]] += amount
    result = list(letters.values())
    result.sort()
    print("part2:", result[-1] - result[0], dict(letters))

part2()


    
