import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/prompt/"""

# CLI Option with Customised Prompt


def main(
    name: str,
    lastname: Annotated[str, typer.Option(prompt="Please tell me your last name")],
):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
