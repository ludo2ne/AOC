import os
from time import time
import numpy as np

from src.utils.get_input import import_input

example = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()


def format_dataset(text: str) -> list[str]:
    lines = text.splitlines()

    grid_array = np.array([list(row) for row in lines])

    # Ajouter 3 lignes de points (.) en haut et en bas
    rows, cols = grid_array.shape
    padding_rows = np.full((3, cols), '.')  # Créer un tableau de 3 lignes de points
    grid_with_rows = np.vstack([padding_rows, grid_array, padding_rows])

    # Ajouter 3 colonnes de points (.) au début et à la fin
    padding_cols = np.full((grid_with_rows.shape[0], 3), '.')  # Créer 3 colonnes de points
    final_grid = np.hstack([padding_cols, grid_with_rows, padding_cols])

    return final_grid


def part1(text: str) -> int:
    res = 0
    array = format_dataset(text)

    for i, row in enumerate(array):
        for j, el in enumerate(row):
            if el == 'X':
                if row[j+1] == 'M' and row[j+2] == 'A' and row[j+3] == 'S':
                    res += 1
                if row[j-1] == 'M' and row[j-2] == 'A' and row[j-3] == 'S':
                    res += 1
                if array[i-1][j] == 'M' and array[i-2][j] == 'A' and array[i-3][j] == 'S':
                    res += 1
                if array[i+1][j] == 'M' and array[i+2][j] == 'A' and array[i+3][j] == 'S':
                    res += 1
                if array[i+1][j+1] == 'M' and array[i+2][j+2] == 'A' and array[i+3][j+3] == 'S':
                    res += 1
                if array[i+1][j-1] == 'M' and array[i+2][j-2] == 'A' and array[i+3][j-3] == 'S':
                    res += 1
                if array[i-1][j+1] == 'M' and array[i-2][j+2] == 'A' and array[i-3][j+3] == 'S':
                    res += 1
                if array[i-1][j-1] == 'M' and array[i-2][j-2] == 'A' and array[i-3][j-3] == 'S':
                    res += 1

    return res


def part2(text: str) -> int:
    res = 0
    array = format_dataset(text)

    for i, row in enumerate(array):
        for j, el in enumerate(row):
            if el == 'A':
                if array[i-1][j-1] == 'M' and array[i-1][j+1] == 'M' and array[i+1][j-1] == 'S' and array[i+1][j+1] == 'S':
                    res += 1
                if array[i-1][j-1] == 'M' and array[i+1][j-1] == 'M' and array[i+1][j+1] == 'S' and array[i-1][j+1] == 'S':
                    res += 1
                if array[i+1][j+1] == 'M' and array[i+1][j-1] == 'M' and array[i-1][j+1] == 'S' and array[i-1][j-1] == 'S':
                    res += 1
                if array[i-1][j+1] == 'M' and array[i+1][j+1] == 'M' and array[i-1][j-1] == 'S' and array[i+1][j-1] == 'S':
                    res += 1

    return res


if __name__ == "__main__":
    file_path = os.path.abspath(__file__)
    day_num = int(file_path.split("day")[1].split(".")[0])
    year = int(os.path.basename(os.path.dirname(file_path)))
    import_input(day_num=day_num, year=year)

    input_path = f"data/{year}/day{day_num}.txt"
    text_input = open(input_path, "r").read()

    start_time = time()
    print(f"1. Example :  {part1(example):<20} ({time()-start_time:.3f} s)")
    start_time = time()
    print(f"1. Input   :  {part1(text_input):<20} ({time()-start_time:.3f} s)")

    print("-" * 100)

    start_time = time()
    print(f"2. Example :  {part2(example):<20} ({time()-start_time:.3f} s)")
    start_time = time()
    print(f"2. Input   :  {part2(text_input):<20} ({time()-start_time:.3f} s)")
