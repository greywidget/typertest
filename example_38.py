import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/callback-and-context/"""

# CLI Option Callback
# Register a Callback function to do some validation


def name_callback(value: str):
    if value != "Camila":
        raise typer.BadParameter("Only Camila is allowed")
    return value


def main(name: Annotated[str, typer.Option(callback=name_callback)]):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
