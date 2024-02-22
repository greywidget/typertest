import typer

"""See https://typer.tiangolo.com/tutorial/commands/arguments/"""

# Command CLI arguments.
# These work just the same way they did for our simpler CLI application
# with a single command

app = typer.Typer()


@app.command()
def create(username: str):
    print(f"Creating user: {username}")


@app.command()
def delete(username: str):
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
