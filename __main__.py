import requests
import traceback
from src.transformations import TransformFromLine, TransformFromColumn
from src.solver import solver


if __name__ == "__main__":
    # r = requests.get("https://sudoku-api.vercel.app/api/dosuku").json()
    # sudoku = r['newboard']['grids'][0]['value']
    sudoku = [
        [1, 0, 0, 0, 0, 7, 0, 9, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 8],
        [0, 0, 9, 6, 0, 0, 5, 0, 0],
        [0, 0, 5, 3, 0, 0, 9, 0, 0],
        [0, 1, 0, 0, 8, 0, 0, 0, 2],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 3, 0, 0],
    ]
    # solution = r['newboard']['grids'][0]['solution']
    sudoku = TransformFromLine(sudoku)
    try :
        solver(sudoku)
    except :
        print(traceback.format_exc())
        print("Error: The sudoku is not solvable")
