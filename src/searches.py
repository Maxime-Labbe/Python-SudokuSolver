def searchInCase(possibleNumbers, line, tab) :
    numbers = [0] * 9
    index = [[],[],[],[],[],[],[],[],[]]
    for k in range(9) :
        for elem in possibleNumbers[line][tab][k] :
            if (elem != -1) :
                numbers[elem - 1] += 1
                index[elem - 1].append(k)
    if (numbers.count(1) >= 1) :
        return numbers.index(1) + 1, index[numbers.index(1)][0]
    return 0, 0
    
def searchPossibleNumbers(sudoku, lineSudoku, columnSudoku, size) :
    possibleNumbers = []
    for i in range(size) : 
        possibleNumbers.append([])
        for j in range(size):
            possibleNumbers[i].append([])
            for k in range(9):
                possibleNumbers[i][j].append([])
                for m in range(9):
                    if (sudoku[i][j][k] != 0) :
                        possibleNumbers[i][j][k].append(-1)
                        break
                    else :
                        if (not (m + 1 in lineSudoku[i * 3 + k // 3]) and not (m + 1 in columnSudoku[j * 3 + k % 3]) and not (m + 1 in sudoku[i][j])) :
                            possibleNumbers[i][j][k].append(m+1)
    return possibleNumbers

def searchLowestPossibility(possibleNumbers, size) :
    lowest = 10
    lowestIndex = [0,0,0]
    for i in range(size) :
        for j in range(size) :
            for k in range(9) :
                if (len(possibleNumbers[i][j][k]) < lowest and len(possibleNumbers[i][j][k]) > 1) :
                    lowest = len(possibleNumbers[i][j][k])
                    lowestIndex = [i,j,k]
    return lowestIndex