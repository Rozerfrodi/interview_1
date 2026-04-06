from reports.median_coffee import MedianCoffeeReport


def test_median_calculation():
    data = [
        {"student": "Ivan", "coffee_spent": 100},
        {"student": "Ivan", "coffee_spent": 300},
        {"student": "Ivan", "coffee_spent": 200},
    ]

    report = MedianCoffeeReport()
    result = report.generate(data)

    assert "Ivan" in result
    assert "200" in result

