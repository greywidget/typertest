import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/arguments/help/"""

# It might not be a good idea, but you can Hide a CLI argument from the
# Help Text. This causes it to not show up in the `Arguments` section
# in the help text. (It is still shown in the `Usage` section)


def main(name: Annotated[str, typer.Argument(hidden=True)] = "World"):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
