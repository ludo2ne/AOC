import os
import sys

import dotenv
import requests

dotenv.load_dotenv(override=True)


def import_input(day_num, year):
    base_dir = "data"
    year_dir = os.path.join(base_dir, str(year))
    os.makedirs(year_dir, exist_ok=True)

    input_path = f"{year_dir}/day{day_num}.txt"

    if not os.path.isfile(input_path):
        cookies = {"session": os.environ["SESSION"]}

        req = requests.get(
            f"https://adventofcode.com/{year}/day/{day_num}/input",
            cookies=cookies,
        )

        if req.status_code == 200:
            with open(input_path, "w") as file:
                file.write(req.text.rstrip("\n"))
        else:
            print(
                f"Failed to download the file. Status code: {req.status_code}",
                file=sys.stderr,
            )
