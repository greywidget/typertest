import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/name/"""

# CLI Option with a Custom Name
# By default Typer creates the CLI option name from the function parameter
# eg. a parameter value of `user_name` will by default be named `--user-name`
# But you can customise this:


def main(user_name: Annotated[str, typer.Option("--name")]):
    """
    The `user_name` parameter is customised to `--name`
    (instead of the default `--user-name`)
    """

    print(f"Hello {user_name}")


if __name__ == "__main__":
    typer.run(main)
