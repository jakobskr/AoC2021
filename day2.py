

def part1():
    hor, depth = (0,0)
    for line in open("day2_input", "r"):
        cmd , arg = line.strip().split(" ")
        arg = int(arg)
        if cmd == "forward":
            hor += arg
        elif cmd == "down":
            depth += arg
        elif cmd == "up":
            depth -= arg
    print(hor, depth, hor*depth)

def part2():
    hor, depth = (0,0)
    aim = 0
    for line in open("day2_input", "r"):
        cmd , arg = line.strip().split(" ")
        arg = int(arg)
        if cmd == "forward":
            depth += arg * aim
            hor += arg
        elif cmd == "down":
            aim += arg
        elif cmd == "up":
            aim -= arg
    print(hor, depth, hor*depth)

part1()
part2()