import typer

"""See https://typer.tiangolo.com/tutorial/commands/name/"""

# Custom Command Name
# By default, the command names are generated from the function name
# Suppose this would cause a clash with an existing function in your code
# If you still want to use that name, you can rename the actual function
# but pass a name in the `@app.command()` decorator

# In the example below, we want our commands to bi called `create` and
# `delete`, but that would cause a name clash. So we can achieve what we
# want as shown below

app = typer.Typer()


@app.command("create")
def cli_create_user(username: str):
    print(f"Creating user: {username}")


@app.command("delete")
def cli_delete_user(username: str):
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
