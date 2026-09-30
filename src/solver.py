import copy
import time
from src.transformations import TransformIntoLine, TransformIntoColumn, displayGrid
from src.checks import VerifyEnd, checkDeadEnd, checkLoop
from src.searches import searchPossibleNumbers, searchLowestPossibility, searchInCase, eliminateNakedPairs, resetTimingStats, getTimingStats

def replaceNumbers(sudoku, possibleNumbers, size) :
    newSudoku = copy.deepcopy(sudoku)
    for i in range(size) :
        for j in range(size) :
            for k in range(size**2) :
                if (len(possibleNumbers[i][j][k]) == 1 and possibleNumbers[i][j][k][0] != -1) :
                    newSudoku[i][j][k] = possibleNumbers[i][j][k][0]
            numberFound, index = searchInCase(possibleNumbers, i, j)
            if (numberFound != 0 and not (numberFound in newSudoku[i][j])) :
                newSudoku[i][j][index] = numberFound
    return newSudoku

def simulate(sudoku, size, possibleNumbers, index, loops) :
    index += 1
    newPossibleNumbers = copy.deepcopy(possibleNumbers)
    newSudoku = copy.deepcopy(sudoku)
    lowestIndex = searchLowestPossibility(newPossibleNumbers, size)
    randomNumber = newPossibleNumbers[lowestIndex[0]][lowestIndex[1]][lowestIndex[2]][0]
    newSudoku[lowestIndex[0]][lowestIndex[1]][lowestIndex[2]] = randomNumber  
    while (not VerifyEnd(newSudoku, size)) :
        lineSudoku = TransformIntoLine(newSudoku)
        columnSudoku = TransformIntoColumn(newSudoku)
        newPossibleNumbers = searchPossibleNumbers(newSudoku, lineSudoku, columnSudoku, size)
        newPossibleNumbers = eliminateNakedPairs(newPossibleNumbers, size)
        if (newSudoku == replaceNumbers(newSudoku,newPossibleNumbers,size) and checkDeadEnd(newPossibleNumbers, size)) :
            if index == 1 or index in loops:
                possibleNumbers[lowestIndex[0]][lowestIndex[1]][lowestIndex[2]].remove(randomNumber)
                newSudoku = copy.deepcopy(sudoku)
                newPossibleNumbers = copy.deepcopy(possibleNumbers)
                lowestIndex = searchLowestPossibility(newPossibleNumbers, size)
                randomNumber = newPossibleNumbers[lowestIndex[0]][lowestIndex[1]][lowestIndex[2]][0]
                newSudoku[lowestIndex[0]][lowestIndex[1]][lowestIndex[2]] = randomNumber
            if index != 1:
                return newSudoku
        elif (checkLoop(newPossibleNumbers, size)) :
            loops.append(index)
            newSudoku = simulate(newSudoku, size, newPossibleNumbers, index,loops)
            loops.remove(index)
        else :
            newSudoku = replaceNumbers(newSudoku, newPossibleNumbers, size)
    return newSudoku

def solver(sudoku) :
    resetTimingStats()
    start_time = time.perf_counter()
    lastTime = start_time
    size = 3
    lineSudoku = []
    columnSudoku = []        
    displayGrid(sudoku, size)
    while (not VerifyEnd(sudoku, size)) :
        lineSudoku = TransformIntoLine(sudoku)
        columnSudoku = TransformIntoColumn(sudoku)
        possibleNumbers = searchPossibleNumbers(sudoku, lineSudoku, columnSudoku, size)
        possibleNumbers = eliminateNakedPairs(possibleNumbers, size)
        sudoku = replaceNumbers(sudoku, possibleNumbers, size)
        if (checkLoop(possibleNumbers, size)) :
            newSudoku = copy.deepcopy(sudoku)
            result = simulate(newSudoku, size, possibleNumbers, index=0, loops=[])
            if result != False:
                sudoku = result
        else:
            sudoku = replaceNumbers(sudoku, possibleNumbers, size)
        if (time.perf_counter() - lastTime > 1) :
            displayGrid(sudoku, size)
            lastTime = time.perf_counter()
    displayGrid(sudoku, size)
    print("Execution time: %.6f seconds" % (time.perf_counter() - start_time))
    for name, stats in getTimingStats().items():
        calls = stats["calls"]
        total = stats["seconds"]
        average = total / calls if calls else 0.0
        print(f"{name}: {calls} calls, {total:.6f} seconds total, {average:.6f} seconds per call")