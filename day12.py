
from collections import Counter
def explore(cave,path):
    path = path[:]
    path.append(cave)
    if cave == "end":
        #print("end of path", path)
        paths.append(path)
        return
    
    for c in caves[cave]:
        #print(cave,c, path)
        if c not in path:
            explore(c,path)
        elif c in path and c.islower() and 2 not in Counter(list(filter(lambda x: x.islower() , path))).values() and c != "start":
            explore(c,path)
        elif c in path and c.isupper():
            explore(c,path)

#2 > len(list(filter(lambda x: x == c , path))) saving this for later : )

caves = {}
paths = []

for line in open("day12_input","r"):
    s, e = line.strip().split("-")
    print(s,e)
    if s in caves:
        caves[s] += [e]
    else:
        caves[s] = [e]
    if e in caves:
        caves[e] += [s]
    else:
        caves[e] = [s]
print(caves)
explore("start", [])
print("number of paths:" , len(paths))
