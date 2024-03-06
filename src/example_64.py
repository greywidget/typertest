import typer

"""See https://typer.tiangolo.com/tutorial/commands/context/"""

"""
Using the Context

Typer uses Click underneath. Every Click app has a special object called a
`Context` that is normally hidden.

But you can access the context by declaring a function parameter of type
`typer.Context`

Suppose you want to execute some logic in a Typer callback depending on the
subcommand that is being called:
"""


app = typer.Typer()


@app.command()
def create(username: str):
    print(f"Creating user: {username}")


@app.command()
def delete(username: str):
    print(f"Deleting user: {username}")


@app.callback()
def main(ctx: typer.Context):
    """
    Manage users in the awesome CLI app.
    """
    print(f"About to execute command: {ctx.invoked_subcommand}")


if __name__ == "__main__":
    app()
