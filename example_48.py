import typer

"""See https://typer.tiangolo.com/tutorial/commands/help/"""

# Overwrite Command Help
# It's best just to use the docstrings for Help, but if for some reason
# you wanted to overwrite it, you can use the `help` function argument
# passed to `@app.command()`

app = typer.Typer()


@app.command(help="Create a new user with USERNAME.")
def create(username: str):
    """
    Some internal utility function to create.
    """
    print(f"Creating user: {username}")


@app.command(help="Delete a user with USERNAME.")
def delete(username: str):
    """
    Some internal utility function to delete.
    """
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
