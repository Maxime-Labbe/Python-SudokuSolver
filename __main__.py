import requests
from src.transformations import TransformFromLine
from src.solver import solver


if __name__ == "__main__":
    r = requests.get("https://sudoku-api.vercel.app/api/dosuku").json()
    sudoku = r['newboard']['grids'][0]['value']
    solution = r['newboard']['grids'][0]['solution']
    sudoku = TransformFromLine(sudoku)
    try :
        solver(sudoku)
    except :
        print("Error: The sudoku is not solvable")
