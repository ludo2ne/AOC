import os
from itertools import pairwise
from time import time

from src.utils.get_input import import_input

example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def safe_report(levels: list[int]) -> bool:
    pairs = list(pairwise(levels))

    if levels != sorted(levels):
        pairs = [tuple(reversed(tup)) for tup in pairs]

    return all(el[1] > el[0] and el[0] + 3 >= el[1] for el in pairs)


def part1(text):
    res = 0
    lines = text.splitlines()

    for index, line in enumerate(lines):
        line_splited = list(map(int, line.split(" ")))

        if safe_report(line_splited):
            res += 1

    return res


def part2(text):
    res = 0
    lines = text.splitlines()

    for index, line in enumerate(lines):
        line_splited = list(map(int, line.split(" ")))

        if safe_report(line_splited):
            res += 1
        else:
            for i in range(len(line_splited)):
                line_copy = line_splited.copy()
                line_copy.pop(i)
                if safe_report(line_copy):
                    res += 1
                    break

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
