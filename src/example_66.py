import typer

"""See https://typer.tiangolo.com/tutorial/commands/context/"""

"""
Using the Context

Exclusive executable callback (see also example_65.py)

We might not always want the callback to be executed if there's already 
another command to be executed. To control this, we can get the `typer.Context`
and check if there's an invoked command in `ctx.invoked_subcommand`
"""


app = typer.Typer()


@app.command()
def create(username: str):
    print(f"Creating user: {username}")


@app.command()
def delete(username: str):
    print(f"Deleting user: {username}")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Manage users in the awesome CLI app.
    """
    if ctx.invoked_subcommand is None:
        print("Initializing database")


if __name__ == "__main__":
    app()
