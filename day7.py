import timeit



def calculateFuel2(x, data):
    fuel = 0
    return sum(list(map (lambda y : sum(range(1,abs(x - y) + 1)), data )))
    

def part2_loop(data, ceiling):
    fuelData2 = [calculateFuel2(x,data) for x in range(0, ceiling)]
    print(min(fuelData2), fuelData2.index(min(fuelData2)))


def part2_map(data,ceiling):
    fuelData3 = list(map(lambda x , y : sum(list(map (lambda y : sum(range(1,abs(x - y) + 1)), data ) )) , range(0,ceiling + 1), data))
    print(min(fuelData3), fuelData3.index(min(fuelData3)))


def calculateFuel(x ,data):
    fuel = 0
    for val in data:
        fuel += abs(x - val)
    return fuel

data = [int(x) for x in open("day7_input", "r").read().strip().split(",")]
#data = [16,1,2,0,4,2,7,1,2,14]

ceiling = max(data) + 1

print(data)
fuelData = [calculateFuel(x,data) for x in range(0, ceiling)]
print(min(fuelData), fuelData.index(min(fuelData)))
fuelData3 = list(map(lambda x , y : sum(list(map (lambda y : sum(range(1,abs(x - y) + 1)), data ) )) , range(0,ceiling + 1), data))
print(min(fuelData3), fuelData3.index(min(fuelData3)))


print(timeit.timeit('part2_loop(data, ceiling)', globals=globals(), number=1))
print(timeit.timeit('part2_map(data, ceiling)', globals=globals(), number=1))



