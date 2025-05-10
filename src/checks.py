from src.transformations import TransformIntoLine, TransformIntoColumn
def VerifyEnd(sudoku, size) :
    lineSudoku = TransformIntoLine(sudoku)
    columnSudoku = TransformIntoColumn(sudoku)
    for i in range(size) :
        for j in range(size) :
            for k in range(9) :
                if sudoku[i][j][k] == 0 :
                    return False
                if sudoku[i][j].count(sudoku[i][j][k]) > 1 or lineSudoku[i * 3 + k // 3].count(sudoku[i][j][k]) > 1 or columnSudoku[j * 3 + k % 3].count(sudoku[i][j][k]) > 1 :
                    return False
    return True

def checkDeadEnd(possibleNumbers, size) :
    for i in range(size) :
        for j in range(size) :
            for k in range(9) :
                if (len(possibleNumbers[i][j][k]) > 1) :
                    return False
    return True

def checkLoop(possibleNumbers, size) :
    for i in range(size) :
        for j in range(size) :
            for k in range(9) :
                if (len(possibleNumbers[i][j][k]) == 1 and possibleNumbers[i][j][k][0] != -1) :
                    return False
    return True