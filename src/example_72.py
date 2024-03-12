import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/bool/"""

"""
Boolean CLI options

We've previously seen examples of CLI options with `bool` and how Typer
creates `--something` and `--no-something` automatically.
But we can customise those names.

Suppose we want a `--force` CLI option, but no `--no-force`. We can do that
by specifying the exact name we want:
"""


def main(force: Annotated[bool, typer.Option("--force")] = False):
    """
    See how this has `--force`, but no `--no-force`
    """
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    typer.run(main)
