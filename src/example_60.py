import typer

"""See https://typer.tiangolo.com/tutorial/commands/one-or-multiple/"""

"""
If you create a single command as below, Typer is smart enough to create a 
CLI Application with that single function as the main CLI application, not
as a command/subcommand:
"""


app = typer.Typer()


@app.command()
def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
