import typer

"""See https://typer.tiangolo.com/tutorial/subcommands/add-typer/"""

"""
Typer SubCommands - Command Groups

This example uses:
- items.py
- users.py (this file)
- app1.py (which ties them together)

Secondly we create this file for managing users:
"""


app = typer.Typer()


@app.command()
def create(user_name: str):
    print(f"Creating user: {user_name}")


@app.command()
def delete(user_name: str):
    print(f"Deleting user: {user_name}")


if __name__ == "__main__":
    app()
