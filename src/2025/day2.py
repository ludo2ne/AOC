import os
from time import time

from utils.get_input import import_input

example = """11-22,95-115"""
# example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def format_dataset(text: str) -> list[str]:
    el = text.split(",")
    couples = []

    for index, line in enumerate(el):
        couples.append(line.split("-"))

    return couples


def part1(text: str) -> int:
    res = 0
    couples = format_dataset(text)

    for v in couples:
        for j in range(int(v[0]), int(v[1]) + 1):
            js = str(j)
            lj = int(len(js))
            # print(js, lj, end=" ")
            if lj % 2 == 0:
                lj2 = lj // 2
                if js[lj2:] == js[:lj2]:
                    res += j
                # print(js[lj2:], js[:lj2], res)
        # print("---------------")
    return res


def part2(text: str) -> int:
    res = 0
    couples = format_dataset(text)

    for v in couples:
        for j in range(int(v[0]), int(v[1]) + 1):
            js = str(j)
            lj = int(len(js))

            for i in range(2, lj + 1):
                print(js, i)

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
    # start_time = time()
    # print(f"1. Input   :  {part1(text_input):<20} ({time() - start_time:.3f} s)")

    print("-" * 100)

    start_time = time()
    print(f"2. Example :  {part2(example):<20} ({time() - start_time:.3f} s)")
    # start_time = time()
    # print(f"2. Input   :  {part2(text_input):<20} ({time()-start_time:.3f} s)")
