import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/options/prompt/"""

# CLI Option Prompt
# I was curious to see if you could prompt an Argument eg:
# `typer.Argument(prompt=True)` and this threw an exception
# I wonder if it has to do with the fact that Options are associated
# with keywords?


def main(name: str, lastname: Annotated[str, typer.Option(prompt=True)]):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
