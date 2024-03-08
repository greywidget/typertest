import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/number/"""

"""
CLI Parameter Types Counter CLI options

You can make a CLI option work as a counter with the `counter` parameter:
"""


def main(verbose: Annotated[int, typer.Option("--verbose", "-v", count=True)] = 0):
    """
    It means that the CLI option will be like a boolean flag, e.g. `--verbose`

    And the value you receive in the function will be the amount of times that
    `--verbose` was added:

    E.g try `python example_71.py --verbose --verbose`
    (or `python example_71.py -v -v -v`)
    (or `python example_71.py -vvv`)
    """
    print(f"Verbose level is {verbose}")


if __name__ == "__main__":
    typer.run(main)
