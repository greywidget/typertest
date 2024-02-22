import typer

"""See https://typer.tiangolo.com/tutorial/commands/"""

# A CLI application with multiple commands

app = typer.Typer()


@app.command()
def create():
    print("Creating user: Hiro Hamada")


@app.command()
def delete():
    print("Deleting user: Hiro Hamada")


if __name__ == "__main__":
    app()
