import typer

"""See https://typer.tiangolo.com/tutorial/commands/one-or-multiple/"""

"""
Using the callback to document
How that you are using a callback just to have a single command, you might as
well use it to add documentation for your new app:
"""


app = typer.Typer()


@app.command()
def create():
    print("Creating user: Hiro Hamada")


@app.callback()
def callback():
    """
    Creates a single user Hiro Hamada.

    In the next version it will create 5 users more.
    """


if __name__ == "__main__":
    app()
