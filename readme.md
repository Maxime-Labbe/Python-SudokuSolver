# Sudoku Solver

This project is a sudoku solver, you just have to log it in and the script will resolve it for you.

## Table of Contents

- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## How It Works

1. It transforms the sudoku into differents shapes to make it easier for the script for the next step.

2. It searches all the possible numbers by doing simple search like 'Is this number in the square ?', 'Is this number in the line ?' and 'Is this number in the column ?', repetiting this for all the cell in the sudoku.

3. By using the numbers found above, it process a script that uses a technic to eliminate numbers called (Naked Pairs).

4. Then it replaces the empty cells where there is only one possibility that has been found and performs a last check after replacing all the numbers in a square, to see if a number can be placed at only one cell in the square.

5. If the last step returned a sudoku that is different from the one that got in, then it repeat from step 1. Else, it goes to step 6.

6. It picked the cell with the less possible numbers that can be placed in it and take the lowest number to try if it works like this, then it repeat itself from step 1 until there is nothing that can be placed in the sudoku anymore which makes go to step 7.

7. If the sudoku is well completed, it returns the result. Else it goes back to the last time it picked a random number, it removes the number from the possibilities and try an other one. And finally goes back to the step 1.

## Installation

### Prerequisites

- Python 3.x

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/Maxime-Labbe/Python-SudokuSolver
    cd Python-SudokuSolver
    ```

2. Enter your Sudoku (OPTIONAL):

    You can see the way to write the sudoku in [Write my own](#write-my-own).

3. Start the script:

    ```bash
    python __main__.py
    ```

4. And now, just wait for the result (it should take less than a second).

## Usage

You ave 2 ways to use the script call from the API that I've already used or enter it yourself.

### From the API

You just have to execute the code if you want to use this API or enter a new one (I can't assure that the way your sudoku is written is supported by my script but you can transform it from various way, see [Write my own](#write-my-own))

### Write my own

There are 3 ways to write sudoku that the script support :

Used example :

    -----------------------------------------
    || 6 | 7 | 9 || 3 | 1 | 2 || 4 | 5 | 8 ||
    || 3 | 8 | 2 || 5 | 7 | 4 || 9 | 6 | 1 ||
    || 5 | 4 | 1 || 6 | 9 | 8 || 2 | 3 | 7 ||
    -----------------------------------------
    || 2 | 6 | 8 || 9 | 4 | 7 || 3 | 1 | 5 ||
    || 7 | 1 | 3 || 2 | 5 | 6 || 8 | 9 | 4 ||
    || 4 | 9 | 5 || 1 | 8 | 3 || 7 | 2 | 6 ||
    -----------------------------------------
    || 1 | 5 | 4 || 8 | 3 | 9 || 6 | 7 | 2 ||
    || 8 | 3 | 6 || 7 | 2 | 1 || 5 | 4 | 9 ||
    || 9 | 2 | 7 || 4 | 6 | 5 || 1 | 8 | 3 ||
    -----------------------------------------

#### By Line

```python
line_example = [
    [6, 7, 9, 3, 1, 2, 4, 5, 8],
    [3, 8, 2, 5, 7, 4, 9, 6, 1],
    [5, 4, 1, 6, 9, 8, 2, 3, 7],
    [2, 6, 8, 9, 4, 7, 3, 1, 5],
    [7, 1, 3, 2, 5, 6, 8, 9, 4],
    [4, 9, 5, 1, 8, 3, 7, 2, 6],
    [1, 5, 4, 8, 3, 9, 6, 7, 2],
    [8, 3, 6, 7, 2, 1, 5, 4, 9],
    [9, 2, 7, 4, 6, 5, 1, 8, 3]
    ]
```

#### By Column

```python
column_example = [
    [6, 3, 5, 2, 7, 4, 1, 8, 9],
    [7, 8, 4, 6, 1, 9, 5, 3, 2],
    [9, 2, 1, 8, 3, 5, 4, 6, 7],
    [3, 5, 6, 9, 2, 1, 8, 7, 4],
    [1, 7, 9, 4, 5, 8, 3, 2, 6],
    [2, 4, 8, 7, 6, 3, 9, 1, 5],
    [4, 9, 2, 3, 8, 7, 6, 5, 1],
    [5, 6, 3, 1, 9, 2, 7, 4, 8],
    [8, 1, 7, 5, 4, 6, 2, 9, 3]]
```

#### By Line-Square

```python
line_square_example = [
    [
        [6, 7, 9, 3, 8, 2, 5, 4, 1],
        [3, 1, 2, 5, 7, 4, 6, 9, 8],
        [4, 5, 8, 9, 6, 1, 2, 3, 7]
    ],
    [
        [2, 6, 8, 7, 1, 3, 4, 9, 5],
        [9, 4, 7, 2, 5, 6, 1, 8, 3],
        [3, 1, 5, 8, 9, 4, 7, 2, 6]
    ], 
    [
        [1, 5, 4, 8, 3, 6, 9, 2, 7],
        [8, 3, 9, 7, 2, 1, 4, 6, 5],
        [6, 7, 2, 5, 4, 9, 1, 8, 3]
    ]]
```

#### Possible transformations

There is multiple transformations possible(knowing that the main function uses Line-Square) :
- Line-Square -> Column (TransformIntoColumn)
- Line-Square -> Line (TransformIntoLine)
- Column -> Line-Square (TransformFromColumn)
- Line -> Line-Square (TransformFromLine)

## Project Structure

```bash
Python-Socket-Messaging/
├── src
    ├── checks.py
    ├── searches.py
    ├── solver.py
    └── transformations.py
├── __main__.py
└── README.md
```