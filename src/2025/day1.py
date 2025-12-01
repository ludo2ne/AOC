import os
from time import time

from utils.get_input import import_input

example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def format_dataset(text: str) -> list[str]:
    return text.splitlines()


def part1(text: str) -> int:
    res = 0

    dial = 50

    for v in format_dataset(text):
        if v[0] == "L":
            dial -= int(v[1:])
        elif v[0] == "R":
            dial += int(v[1:])

        if dial >= 100 or dial < 0:
            dial = dial % 100

        if dial == 0:
            res += 1

    return res


def part2(text: str) -> int:
    res = 0

    dial = 50
    dial_prec = 50

    for v in format_dataset(text):
        dial_prec = dial
        v1 = int(v[1:])

        if v1 > 100:
            res += v1 // 100
            v1 = v1 % 100

        if v[0] == "L":
            dial -= v1
        elif v[0] == "R":
            dial += v1

        if dial >= 100 or dial <= 0:
            dial = dial % 100
            if dial_prec != 0:
                res += 1

        print(dial_prec, v, v1, dial, res)

    return res


if __name__ == "__main__":
    file_path = os.path.abspath(__file__)
    day_num = int(file_path.split("day")[1].split(".")[0])
    year = int(os.path.basename(os.path.dirname(file_path)))
    import_input(day_num=day_num, year=year)

    input_path = f"data/{year}/day{day_num}.txt"
    text_input = open(input_path, "r").read()

    start_time = time()
    print(f"1. Example :  {part1(example):<20} ({time() - start_time:.3f} s)")
    start_time = time()
    print(f"1. Input   :  {part1(text_input):<20} ({time() - start_time:.3f} s)")

    print("-" * 100)

    start_time = time()
    print(f"2. Example :  {part2(example):<20} ({time() - start_time:.3f} s)")
    start_time = time()
    print(f"2. Input   :  {part2(text_input):<20} ({time() - start_time:.3f} s)")
