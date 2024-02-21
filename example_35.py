import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/options/name/"""

# CLI Option Short Name Only


def main(user_name: Annotated[str, typer.Option("-n")]):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    typer.run(main)
