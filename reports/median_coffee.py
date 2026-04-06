from statistics import median
from tabulate import tabulate
from .base import BaseReport


class MedianCoffeeReport(BaseReport):
    name = "median-coffee"

    def generate(self, data: list[dict]) -> str:
        student_spending = {}

        for row in data:
            student = row["student"]
            spent = row["coffee_spent"]
            if student not in student_spending:
                student_spending[student] = []
            student_spending[student].append(spent)

        result = []
        for student, values in student_spending.items():
            med = median(values)
            result.append((student, med))

        result.sort(key=lambda x: x[1], reverse=True)

        table = tabulate(result, headers=["student", "median_coffee"], tablefmt="grid")

        return table
