import os
from time import time

from src.utils.get_input import import_input

example = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
example2 = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)


def apply_mul(text) -> int:
    res = 0

    split_line = text.split("mul(")

    for instr in split_line:
        x = instr.split(")")[0].split(",")

        if len(x) == 2 and x[0].isdigit() and x[1].isdigit():
            # print(f"{instr:<25}  {x[0]}  {x[1]}")
            res += int(x[0]) * int(x[1])

    return res


def part1(text: str) -> int:
    return apply_mul(text)


def part2(text: str) -> int:
    dont = text.split("don't()")

    res = apply_mul(dont[0])

    for d in dont[1:]:
        dodo = d.split("do()")

        if len(dodo) > 1:
            for todo in dodo[1:]:
                res += apply_mul(todo)

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
    print(f"2. Example :  {part2(example2):<20} ({time()-start_time:.3f} s)")
    start_time = time()
    print(f"2. Input   :  {part2(text_input):<20} ({time()-start_time:.3f} s)")
