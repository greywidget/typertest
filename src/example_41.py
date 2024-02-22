from typing import Optional

import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/version/"""

# The previous example (example_40) was OK, but would not work
# correctly if another CLI option was declared before --version
# and had a callback which could exit the program early
# This example illustrates that flaw.

# Note that the order of the passed parameters is important:
# `python .\example_41.py --version --name Craig` works OK
# `python .\example_41.py --name Craig --version` exits early
# and does not print the version


__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise typer.Exit()


def name_callback(name: str):
    if name != "Camila":
        raise typer.BadParameter("Only Camila is allowed")


def main(
    name: Annotated[str, typer.Option(callback=name_callback)],
    version: Annotated[
        Optional[bool], typer.Option("--version", callback=version_callback)
    ] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
