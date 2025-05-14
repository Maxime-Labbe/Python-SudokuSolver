def TransformIntoColumn(sudoku) :
    sudokuColumn = []
    for i in range(9) :
        sudokuColumn.append([])
        for j in range(9) :
            sudokuColumn[i].append(sudoku[j // 3][i // 3][(j % 3)*3 + i % 3])
    return sudokuColumn

def TransformIntoLine(sudoku) :
    sudokuLine = []
    for i in range(9) :
        sudokuLine.append([])
        for j in range(9) :
            sudokuLine[i].append(sudoku[i // 3][j // 3][(i % 3)*3 + j % 3])
    return sudokuLine

def TransformFromLine(sudokuLine) :
    sudoku = []
    for i in range(3) :
        sudoku.append([])
        for j in range(3) :
            sudoku[i].append([])
            for k in range(9) :
                sudoku[i][j].append(sudokuLine[k // 3 + i * 3][k % 3 + j * 3])
    return sudoku

def TransformFromColumn(sudokuColumn) :
    sudoku = []
    for i in range(3) :
        sudoku.append([])
        for j in range(3) :
            sudoku[i].append([])
            for k in range(9) :
                sudoku[i][j].append(sudokuColumn[k // 3 + j * 3][k % 3 + i * 3])
    return sudoku

def displayGrid(sudoku,size) :
    print("-" * (size * 13 + 2))
    for i in range(size) :
        for j in range(size) :
            print("||", end = " ")
            for k in range(9) :
                if (k % 3 == 2) :
                    print(sudoku[i][k // 3][j * 3 + k % 3] if sudoku[i][k // 3][j * 3 + k % 3] != 0 else " ", end = " || ")
                else:
                    print(sudoku[i][k // 3][j * 3 + k % 3] if sudoku[i][k // 3][j * 3 + k % 3] != 0 else " ", end = " | ")
            print()
            if (j % 3 == 2) :
                print("-" * (size * 13 + 2), end="")
        print()