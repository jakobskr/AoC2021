
def calculateWinningBoard(board, draw):
    sum = 0
    for row in board:
        for cell in row:
            if not cell[1]:
                sum += cell[0]
    return sum * draw

def playLastBoard(i, draws, board):
    for draw in draws[i:]:
        checkNumber(board, draw)
        if checkBingo(board):
            return calculateWinningBoard(board, draw)

def checkBingo(board):
    for row in board:
        bingo = True
        for cell in row:
            if not cell[1]:
                bingo = False
                break
        if bingo:
            return True
        
    for i in range(0,4):
        bingo = True
        for j in range(0,4):
            if not board[j][i][1]:
                bingo = False
                break
        if bingo:
            return True

    return False

def checkNumber(board, number):
    for row in board:
        for cell in enumerate(row):
            if cell[1][0] == number:
                row[cell[0]] = (cell[1][0], True)
                return True

f = open("day4_input", "r")

draws = [int(x) for x in f.readline().strip().split(",")]
f.readline()
print(draws)
#line = f.read()
boards = []
while True:
    board = []
    for i in range(0,5):
        board.append([(int(x), False) for x in f.readline().strip().split()])
    print(board)
    
    boards.append(board)
    line = f.readline()

    if not line:
        print("no more?")
        break

firstWinningBoard = -1
lastWinningBoard = -1
firstFound = False
score = 0
for draw in draws:
    print(draw)
    [checkNumber(board, draw) for board in boards]
    
    bingoStatus = ([checkBingo(board) for board in boards])

    if True in bingoStatus and not firstFound:
        firstWinningBoard = bingoStatus.index(True)
        score = calculateWinningBoard(boards[firstWinningBoard], draw)
        firstFound = True
    
    amountOfTrue = [x for x in bingoStatus if x]
    if len(amountOfTrue) == len(boards) - 1:
        lastWinningBoard = bingoStatus.index(False)
        print("last board found" , lastWinningBoard)
        cur = draws.index(draw)
        lastScore = playLastBoard(cur, draws, boards[lastWinningBoard])
        break

print("First winning board score", score , "\n",  boards[firstWinningBoard])
print("last winning board score", lastScore , "\n",  boards[lastWinningBoard])
