import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/arguments/help/"""

# When you declare `name: str`, it is shown in the Help Text as:
# [NAME]
# But you can customise it (as show in the help text) with the
# `metavar` parameter for `typer.Argument()`


def main(name: Annotated[str, typer.Argument(metavar="✨username✨")] = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
