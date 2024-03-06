import typer

"""See https://typer.tiangolo.com/tutorial/commands/context/"""

"""
Using the Context

By default, the callback is only executed right before executing a command.

And if no command is provided, the help message is shown.

But you can make it run even without a subcommand with 
`invoke_without_command=True`

If you run `python example_65.py`, the callback is executed, we don't get the
default help message:
"""


app = typer.Typer()


@app.command()
def create(username: str):
    print(f"Creating user: {username}")


@app.command()
def delete(username: str):
    print(f"Deleting user: {username}")


@app.callback(invoke_without_command=True)
def main():
    """
    Manage users in the awesome CLI app.
    """
    print("Initializing database")


if __name__ == "__main__":
    app()
