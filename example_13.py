import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/arguments/default/"""

# Optional CLI Arguments with defaults


def main(name: Annotated[str, typer.Argument()] = "Mister Pickle"):
    """
    Optional CLI argument with a default.
    Note that this is a STATIC default. See later for dynamic defaults.
    """

    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
