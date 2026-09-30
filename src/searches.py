import time

_TIMING_STATS = {
    "searchPossibleNumbers": {"calls": 0, "seconds": 0.0},
    "eliminateNakedPairs": {"calls": 0, "seconds": 0.0},
}


def resetTimingStats():
    for stats in _TIMING_STATS.values():
        stats["calls"] = 0
        stats["seconds"] = 0.0


def getTimingStats():
    return {name: stats.copy() for name, stats in _TIMING_STATS.items()}


def _recordTiming(name, start):
    stats = _TIMING_STATS[name]
    stats["calls"] += 1
    stats["seconds"] += time.perf_counter() - start


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
    start = time.perf_counter()
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
    _recordTiming("searchPossibleNumbers", start)
    return possibleNumbers

def searchLowestPossibility(possibleNumbers, size) :
    lowest = size**2+1
    lowestIndex = [0,0,0]
    for i in range(size) :
        for j in range(size) :
            for k in range(size**2) :
                length = len(possibleNumbers[i][j][k])
                if (-1 not in possibleNumbers[i][j][k] and length < lowest and length >= 1) :
                    lowest = length
                    lowestIndex = [i,j,k]
                    if lowest == 1 :
                        return lowestIndex
    return lowestIndex

def eliminateNakedPairs(possibleNumbers, size):
    start = time.perf_counter()
    for i in range(size):
        for j in range(size):
            for k in range(size**2):
                for m in range(k + 1, size**2):
                    if possibleNumbers[i][j][k] == possibleNumbers[i][j][m] and len(possibleNumbers[i][j][k]) == 2:
                        for n in range(size**2):
                            if n != k and n != m:
                                for num in possibleNumbers[i][j][k]:
                                    if num in possibleNumbers[i][j][n]:
                                        possibleNumbers[i][j][n].remove(num)
    _recordTiming("eliminateNakedPairs", start)
    return possibleNumbers