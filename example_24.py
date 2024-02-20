import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/arguments/envvar/"""

# You can hide an environment variables from the help text


def main(
    name: Annotated[
        str, typer.Argument(envvar="AWESOME_NAME", show_envvar=False)
    ] = "World",
):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    typer.run(main)
