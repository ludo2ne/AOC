import os
from time import time

from utils.get_input import import_input

example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def format_dataset(text: str) -> list[str]:
    lines = text.splitlines()

    fresh = []
    available = []

    for line in lines[: lines.index("")]:
        fresh.append((int(line.split("-")[0]), int(line.split("-")[1])))

    for line in lines[lines.index("") + 1 :]:
        available.append(line)

    return fresh, available


def part1(text: str) -> int:
    res = 0
    fresh, available = format_dataset(text)

    for a in available:
        for f in fresh:
            if f[0] <= int(a) <= f[1]:
                res += 1
                break

    return res


def part2(text: str) -> int:
    res = 0
    fresh, available = format_dataset(text)

    for i in range(len(fresh) - 1, 0, -1):
        fi = fresh[i]
        modif = False
        for j in range(i):
            fj = fresh[j]
            if fi[0] <= fj[0] <= fj[1] <= fi[1]:
                fresh[j] = fresh[i]
                modif = True
                break
            if fj[0] <= fi[0] <= fi[1] <= fj[1]:
                modif = True
                break
            if fi[0] <= fj[0] <= fi[1] <= fj[1]:
                fresh[j] = (fi[0], fj[1])
                modif = True
                break
            if fj[0] <= fi[0] <= fj[1] <= fi[1]:
                fresh[j] = (fj[0], fi[1])
                modif = True
                break
        if modif:
            del fresh[i]
            continue

    for f in fresh:
        res += f[1] - f[0] + 1

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
