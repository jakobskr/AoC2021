

fishies = [0] * 9
for x in open("day6_input","r").read().split(","):
    fishies[int(x)] += 1
print("initial state: ", fishies)

for day in range(1,81):
    tmp = fishies[0]
    for i in range(1 ,len(fishies)):
        fishies[i - 1] = fishies[i]
    fishies[6] += tmp
    fishies[-1] = tmp
print(fishies)
print(sum(fishies))

"""for i in range(1,257):
    print(i)
    for index, fish in enumerate(fishies[:]):
        #print(fish, index)
        if fish > 0:
            fishies[index] -= 1
        else:
            fishies[index] = 6
            fishies.append(8)
    #print("after day {}:".format(i), fishies)



for i in range(1,257):
    print(i)
    for index in range(len(fishies)):
        fish = fishies[index]
        #print(fish, index)
        if fish > 0:
            fishies[index] -= 1
        else:
            fishies[index] = 6
            fishies.append(8)
print(len(fishies))

"""