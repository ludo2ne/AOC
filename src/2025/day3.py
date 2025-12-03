import os
from time import time

from utils.get_input import import_input

example = """987654321111111
811111111111119
234234234234278
818181911112111"""


def format_dataset(text: str) -> list[str]:
    return text.splitlines()


def part1(text: str) -> int:
    res = 0
    lines = format_dataset(text)

    for line in lines:
        v1max = 0
        v2max = 0
        imax = 0
        for i, v in enumerate(line[:-1]):
            if int(v) > v1max:
                v1max = int(v)
                imax = i + 1

        for v2 in line[imax:]:
            v2max = max(v2max, int(v2))

        # print(line, v1max, v2max)

        res += v1max * 10 + v2max

    return res


def part2(text: str) -> int:
    res = 0
    lines = format_dataset(text)

    for line in lines:
        res_str = ""
        istart = 0
        for d in range(11, -1, -1):
            vmax = 0
            imax = 0
            # print(line, istart, d, line[istart:-d], end=" ")
            for i, v in enumerate(line[istart : -d if d != 0 else None]):
                if int(v) > vmax:
                    vmax = int(v)
                    imax = i
            istart += imax + 1
            res_str += str(vmax)
            # print(res_str)
        res += int(res_str)

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
