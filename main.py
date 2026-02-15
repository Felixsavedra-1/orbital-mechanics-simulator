import argparse

from report import render_report


def parse_args():
    parser = argparse.ArgumentParser(
        description="Orbital mechanics simulator and space exploration report."
    )
    parser.add_argument(
        "--section",
        choices=["all", "planets", "earth", "concepts", "mars-base"],
        default="all",
        help="Select which section to display.",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json", "csv"],
        default="text",
        help="Select report output format.",
    )
    parser.add_argument(
        "--output",
        default="",
        help="Optional output file path. If omitted, prints to stdout.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    report_body = render_report(args.section, args.format)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as output_file:
            output_file.write(report_body + "\n")
        print(f"Report written to {args.output}")
    else:
        print(report_body)


if __name__ == "__main__":
    main()
