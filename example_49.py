import typer

"""See https://typer.tiangolo.com/tutorial/commands/help/"""

# Deprecate a Command
# This can be done by marking the parameter with `deprecated=True`
#    The Help text will show that the command is deprecated
#    If the command is used, it will work but will issue a
#    Deprecation Warning

app = typer.Typer()


@app.command()
def create(username: str):
    """
    Create a user.
    """
    print(f"Creating user: {username}")


@app.command(deprecated=True)
def delete(username: str):
    """
    Delete a user.

    This is deprecated and will stop being supported soon.
    """
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
