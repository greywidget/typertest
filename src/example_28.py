import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/options/required/"""

# CLI option are optional by default. But you can make them required
# Just leave the parameter without a default value:
# Note that for the `debug` below, you would have to pass
# --debug or --no-debug


def main(
    name: str,
    lastname: Annotated[str, typer.Option()],
    debug: Annotated[bool, typer.Option()],
):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
