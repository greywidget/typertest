import typer

"""See https://typer.tiangolo.com/tutorial/commands/one-or-multiple/"""

"""
If you add Multiple Commands, Typer will create one CLI command for each
of them:
"""


app = typer.Typer()


@app.command()
def create():
    print("Creating user: Hiro Hamada")


@app.command()
def delete():
    print("Deleting user: Hiro Hamada")


if __name__ == "__main__":
    app()
