import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/arguments/help/"""

# CLI arguments with Help and Defaults


def main(name: Annotated[str, typer.Argument(help="Who to greet")] = "World"):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
