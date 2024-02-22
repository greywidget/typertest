from typing import Optional

import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/version/"""

# First version of --version
# You could use a callback to show the version of your CLI program
# and then terminate.

# Note also below that `--version` is declared explicitly because we
# don't want an automatic --no-version.


__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise typer.Exit()


def main(
    name: Annotated[str, typer.Option()] = "World",
    version: Annotated[
        Optional[bool], typer.Option("--version", callback=version_callback)
    ] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
