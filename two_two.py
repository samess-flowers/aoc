#!env python3
import pyperclip  # type:ignore
import click
import typer
from rich.traceback import install

install(show_locals=True, suppress=[click])


# first intake the report as a list of lists
def get_reports_from_file(file) -> list[list[int]]:
    with open(file) as f:
        reports = []
        for line in f:
            reports.append(list(map(int, line.split())))
        return reports


# evaluate each list
def evaluate_report(report: list[int], retry: bool = False) -> bool:
    if not is_direction(report):
        return False
    for c, i in enumerate(report):
        if c == 0:
            continue
        last = report[c - 1]
        if not is_safe(i, last):
            return False
    else:
        return True


def is_safe(a: int, b: int) -> bool:
    """function to check the distance between numbers tc: o(1)"""
    SAFE_RANGES = set([1, 2, 3])
    if abs(a - b) in SAFE_RANGES:
        return True
    return False


def is_direction(report) -> bool:
    if report == sorted(report):
        return True
    elif report == sorted(report, reverse=True):
        return True
    else:
        return False


def main(file: str = "two.txt") -> None:
    reports = get_reports_from_file(file)
    safe_reports = 0
    for report in reports:
        if evaluate_report(report):
            print(report)
            safe_reports += 1
    pyperclip.copy(safe_reports)
    print(f"copied {safe_reports}")
    ...


if __name__ == "__main__":
    typer.run(main)
