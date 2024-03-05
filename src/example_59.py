import typer

"""See https://typer.tiangolo.com/tutorial/commands/callback/"""

"""
Typer Callback

Adding a callback only for documentation

This can be convenient especially if you have several lines of text, as the
indentation will be handled automatically for you.

Now the callback will be used mainly to extract the docstring for the help text
"""


app = typer.Typer()


@app.callback()
def callback():
    """
    Manage users CLI app.

    Use it with the create command.

    A new user with the given NAME will be created.
    """


@app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
