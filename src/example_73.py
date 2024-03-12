from typing import Optional

import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/bool/"""

"""
Boolean CLI options

Alternate names
Suppose we want to allow setting `--accept`, but the contrary `--no-accept` looks
ugly. We would prefer to have `--accept` and `--reject`.

We can achieve this by passing a single `str` with the 2 names for the `bool`
CLI option, separated by `/`:
"""


def main(accept: Annotated[Optional[bool], typer.Option("--accept/--reject")] = None):
    if accept is None:
        print("I don't know what you want yet")
    elif accept:
        print("Accepting!")
    else:
        print("Rejecting!")


if __name__ == "__main__":
    typer.run(main)
