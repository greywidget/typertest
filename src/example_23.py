import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/arguments/envvar/"""

# You can read multiple environment variables.
# Pass them in a list and they will be checked in order until one if found.
# See Previous example if unsure of how this fits with the argument passed
# and default value.


def main(
    name: Annotated[str, typer.Argument(envvar=["USERNAME", "USERPROFILE"])] = "WIDGET",
):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    typer.run(main)
