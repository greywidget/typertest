import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/arguments/default/"""

# CLI arguments with Help (this example also has docstring help)


def main(name: Annotated[str, typer.Argument(help="The name of the user to greet")]):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
