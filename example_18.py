import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/arguments/help/"""

# You can pass a Custom String to be shown as the default
# (instead of the actual default being shown)


def main(
    name: Annotated[
        str,
        typer.Argument(
            help="Who to greet", show_default="Deadpoolio the amazing's name"
        ),
    ] = "Wade Wilson",
):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
