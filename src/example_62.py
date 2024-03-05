import typer

"""See https://typer.tiangolo.com/tutorial/commands/one-or-multiple/"""

"""
One command and one callback
If you want to create a CLI app with one single command but you still want
it to be a command/subcommand you can just add a callback:
"""


app = typer.Typer()


@app.command()
def create():
    print("Creating user: Hiro Hamada")


@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()
