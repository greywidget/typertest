import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/arguments/help/"""

# If you have installed Rich, you can use `rich_help_panel` to show different
# arguments in different panels


def main(
    name: Annotated[str, typer.Argument(help="Who to greet")],
    lastname: Annotated[
        str, typer.Argument(help="The last name", rich_help_panel="Secondary Arguments")
    ] = "",
    age: Annotated[
        str,
        typer.Argument(help="The user's age", rich_help_panel="Secondary Arguments"),
    ] = "",
):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
