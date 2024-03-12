import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/parameter-types/bool/"""

"""
Boolean CLI options

Only names for `False`
It's probably a bad idea, but you can declare CLI option names to
set the `False` value

To do that, use a space ` ` and a single `/` and pass the negative name
after:
"""


def main(in_prod: Annotated[bool, typer.Option(" /--demo", " /-d")] = True):
    if in_prod:
        print("Running in production")
    else:
        print("Running demo")


if __name__ == "__main__":
    typer.run(main)
