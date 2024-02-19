import random

import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/arguments/default/"""

# Optional CLI Argument with Dynamic Default Value


def get_name():
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])


def main(name: Annotated[str, typer.Argument(default_factory=get_name)]):
    """
    `name` has a dynamic default value
    """

    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
