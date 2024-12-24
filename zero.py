#!env python3
import pyperclip
import click
import typer
import rich
from rich.traceback import install

install(show_locals=True, suppress=[click])


# first intake the report as a list of lists
def get_lines_from_file(file) -> list[str]:
    with open(file) as f:
        return [line.rstrip() for line in f]


def main(file: str) -> None:
    input = get_lines_from_file(file)
    rich.print(input[:10])
    ...


if __name__ == "__main__":
    typer.run(main)
