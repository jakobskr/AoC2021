

start = ["{", "(","<","["]
end = {"{":"}", "(":")", "<":">", "[":"]"}
scores = {")": 3, "]":57, "}":1197, ">":25137}
missingScore = {")": 1, "]":2, "}":3, ">":4}
sum = 0
missingSum = 0
missScores = []

for line in open("day10_input", "r"):
    #print (line)
    stack = []
    corrupted = False
    for s in line.strip():
        if s in start:
            stack.append(s)
        elif end[stack[-1]] == s:
            stack.pop()
        else:
            print("Expected {} but found {} instead".format(end[stack[1]], s))
            sum += scores[s] 
            corrupted = True
            break

    if len(stack) > 0 and not corrupted:
        stack.reverse()
        missingSum = 0
        #print(line, stack)

        for s in stack:
            missingSum *= 5
            missingSum += missingScore[end[s]]
        missScores.append(missingSum)

missScores.sort()
#print(missScores)
print("Corrupted sum:", sum, "Missing sum:", missScores[len(missScores) // 2])

