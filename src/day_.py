import os

from time import time
from utils.get_input import import_input

example = """__paste_here__"""


def format_dataset(text):
    lines = text.splitlines()

    for index, line in enumerate(lines):
        split_line = line.split(' ')

    return split_line


def part1(text):
    res = 0
    format_dataset(text)

    return res


def part2(text):
    res = 0
    format_dataset(text)

    return res


if __name__ == "__main__":
    day_num = "".join([n for n in os.path.basename(__file__) if n.isdigit()])
    import_input(day_num)
    input_path = "data/day" + day_num + ".txt"
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