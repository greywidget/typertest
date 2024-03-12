import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/bool/"""

"""
Boolean CLI options

Short names
Similar to Alternate names, yoe can declare short versions of the names for
these CLI options:

Suppose we want `-f` for `--force` and `-F` for `--no-force`:
"""


def main(force: Annotated[bool, typer.Option("--force/--no-force", "-f/-F")] = False):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    typer.run(main)
