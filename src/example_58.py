import typer

"""See https://typer.tiangolo.com/tutorial/commands/callback/"""

"""
Typer Callback

Overriding a callback
If you added a callback when creating the `typer.Typer()` app, it's 
possible to override it with `@app.callback()`
"""


def callback():
    print("Running a command")


app = typer.Typer(callback=callback)


@app.callback()
def new_callback():
    print("Override callback, running a command")


@app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
