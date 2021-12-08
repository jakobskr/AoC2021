

def part1():
    lens = [2,3,4,7]
    sums = 0
    for line in open("day8_input", "r"):
        input, output = line.split(" | ")
        output = output.split()
        sums += sum(list(map(lambda x : 1 if len(x) in lens else 0,  output)))
    print(sums)

def part2():
    for line in open("day8_input", "r"):
        input, output = line.split(" | ")
        output = output.split()
        print(output)


        break











    
part1()
part2()    