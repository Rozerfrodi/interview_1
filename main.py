from cli import parse_args
from services.parser import load_data
from reports import reports


def main():
    args = parse_args()

    data = load_data(args.files)

    report_class = reports.get(args.report)
    if not report_class:
        raise ValueError(f"Unknown report: {args.report}")

    report = report_class()
    result = report.generate(data)

    print(result)


if __name__ == "__main__":
    main()
