import csv
import os

def load_data(files: list[str]) -> list[dict]:
    data = []

    for file in files:
        if not os.path.exists(file):
            raise FileNotFoundError('File does not exist')
        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                row["coffee_spent"] = int(row["coffee_spent"])
                data.append(row)

    return data
