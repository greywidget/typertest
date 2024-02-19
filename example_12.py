from typing import Optional

import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/arguments/optional/"""

# Optional CLI Arguments
# Remember that by default:
# - CLI options are optional
# - CLI arguments are required


def main(name: Annotated[Optional[str], typer.Argument()] = None):
    """
    `name` is an Optional argument.
    See --help, the [] around NAME indicate that it is optional
    """

    if name is None:
        print("Hello World!")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
