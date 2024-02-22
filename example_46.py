import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/commands/arguments/"""

# Command CLI Options (and Command CLI Arguments)
# Checkout the help for both the main program and its subcommands:
#    python example_46.py --help
#    python example_46.py delete --help

app = typer.Typer()


@app.command()
def create(username: str):
    print(f"Creating user: {username}")


@app.command()
def delete(
    username: str,
    force: Annotated[
        bool, typer.Option(prompt="Are you sure you want to delete the user?")
    ],
):
    if force:
        print(f"Deleting user: {username}")
    else:
        print("Operation cancelled")


@app.command()
def delete_all(
    force: Annotated[
        bool, typer.Option(prompt="Are you sure you want to delete ALL users?")
    ],
):
    if force:
        print("Deleting all users")
    else:
        print("Operation cancelled")


@app.command()
def init():
    print("Initializing user database")


if __name__ == "__main__":
    app()
