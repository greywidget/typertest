import typer

"""Another example based on https://typer.tiangolo.com/tutorial/first-steps/"""

# This example shows how you document your app
# Just add a docstring to your function and it will be used in the help text


def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Ms. {name} {lastname}")
    else:
        print(f"Alright {name}?")


if __name__ == "__main__":
    typer.run(main)
