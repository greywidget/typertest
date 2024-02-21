import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/name/"""

# CLI Option Short Name and Default Name


def main(user_name: Annotated[str, typer.Option("--user-name", "-n")]):
    """
    If you want the Default Name AND a Short Name, you need to
    declare both explicitly
    """

    print(f"Hello {user_name}")


if __name__ == "__main__":
    typer.run(main)
