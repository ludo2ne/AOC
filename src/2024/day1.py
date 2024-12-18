import os

from time import time
from src.utils.get_input import import_input

example = """3   4
4   3
2   5
1   3
3   9
3   3"""


def format_dataset(text):
    lines = text.splitlines()

    left, right = [], []

    for index, line in enumerate(lines):
        left.append(int(line.split('   ')[0]))
        right.append(int(line.split('   ')[1]))

    return left, right


def part1(text):
    total_distance = 0
    left, right = format_dataset(text)

    left.sort()
    right.sort()

    for i in range(0, len(left)):
        total_distance += abs(left[i] - right[i])

    return total_distance


def part2(text):
    similarity_score = 0
    left, right = format_dataset(text)

    for el in left:
        similarity_score += el * right.count(el)

    return similarity_score


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