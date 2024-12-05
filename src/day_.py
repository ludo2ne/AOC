import os
from time import time

from src.utils.get_input import import_input

example = """__paste_here__"""


def format_dataset(text: str) -> list[str]:
    lines = text.splitlines()

    for index, line in enumerate(lines):
        split_line = line.split(" ")

    return split_line


def part1(text: str) -> int:
    res = 0
    format_dataset(text)

    return res


def part2(text: str) -> int:
    res = 0
    format_dataset(text)

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
    # start_time = time()
    # print(f"1. Input   :  {part1(text_input):<20} ({time()-start_time:.3f} s)")

    print("-" * 100)

    # start_time = time()
    # print(f"2. Example :  {part2(example):<20} ({time()-start_time:.3f} s)")
    # start_time = time()
    # print(f"2. Input   :  {part2(text_input):<20} ({time()-start_time:.3f} s)")
