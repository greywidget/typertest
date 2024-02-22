import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/commands/help/"""

# Command Help
# You can add help for the commands in the docstrings and CLI options
# just as before

# Also, the `typer.Typer()` application receives a parameter `help`
# that you can pass with the main help text for your CLI program

app = typer.Typer(help="Awesome CLI user manager.")


@app.command()
def create(username: str):
    """
    Create a new user with USERNAME.
    """
    print(f"Creating user: {username}")


@app.command()
def delete(
    username: str,
    force: Annotated[
        bool,
        typer.Option(
            prompt="Are you sure you want to delete the user?",
            help="Force deletion without confirmation.",
        ),
    ],
):
    """
    Delete a user with USERNAME.

    If --force is not used, will ask for confirmation.
    """
    if force:
        print(f"Deleting user: {username}")
    else:
        print("Operation cancelled")


@app.command()
def delete_all(
    force: Annotated[
        bool,
        typer.Option(
            prompt="Are you sure you want to delete ALL users?",
            help="Force deletion without confirmation.",
        ),
    ],
):
    """
    Delete ALL users in the database.

    If --force is not used, will ask for confirmation.
    """
    if force:
        print("Deleting all users")
    else:
        print("Operation cancelled")


@app.command()
def init():
    """
    Initialize the users database.
    """
    print("Initializing user database")


if __name__ == "__main__":
    app()
