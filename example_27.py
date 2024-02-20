import typer
from typing_extensions import Annotated

"""Another example based on https://typer.tiangolo.com/tutorial/options/help/"""

# CLI option with Hidden Default
# The default value (Wade Wilson) does not show in the help text


def main(fullname: Annotated[str, typer.Option(show_default=False)] = "Wade Wilson"):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    typer.run(main)
