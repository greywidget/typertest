import typer

"""See https://typer.tiangolo.com/tutorial/commands/callback/"""

"""
Typer Callback

Adding a callback on creation. This achieves the sam as with `@app.callback()`
"""


def callback():
    print("Running a command")


app = typer.Typer(callback=callback)


@app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
