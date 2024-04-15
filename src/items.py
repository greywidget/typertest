import typer

"""See https://typer.tiangolo.com/tutorial/subcommands/add-typer/"""

"""
Typer SubCommands - Command Groups

This example uses:
- items.py (this file)
- users.py
- app1.py (which ties them together)

Firstly we create this file for managing items:
"""


app = typer.Typer()


@app.command()
def create(item: str):
    print(f"Creating item: {item}")


@app.command()
def delete(item: str):
    print(f"Deleting item: {item}")


@app.command()
def sell(item: str):
    print(f"Selling item: {item}")


if __name__ == "__main__":
    app()
