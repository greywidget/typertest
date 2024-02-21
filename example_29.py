import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/options/prompt/"""

# CLI Option Prompt


def main(name: str, lastname: Annotated[str, typer.Option(prompt=True)]):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
