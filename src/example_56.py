import typer

"""See https://typer.tiangolo.com/tutorial/commands/callback/"""

"""Typer Callback
When you create an `app = typer.Typer()` it works as a group of commands
And you can create multiple commands with it. Each of those commands can
have their own CLI parameters

But as those CLI parameters are handled by each of those commands, they
don't allow us to create CLI parameters for the main CLI application itself.

But we can use `@app.callback()` for that.

It's very similar to `@app.command()` but it declares CLI parameters for the
main CLI application (before the commands)

"""

app = typer.Typer()
state = {"verbose": False}


@app.command()
def create(username: str):
    if state["verbose"]:
        print("About to create a user")
    print(f"Creating user: {username}")
    if state["verbose"]:
        print("Just created a user")


@app.command()
def delete(username: str):
    if state["verbose"]:
        print("About to delete a user")
    print(f"Deleting user: {username}")
    if state["verbose"]:
        print("Just deleted a user")


@app.callback()
def main(verbose: bool = False):
    """
    Manage users in the awesome CLI app.

    After getting the `--verbose` flag, we modify a global `state`, and we
    use it in the other commands. (There are other ways to achieve the same
    thing, but this will suffice for this example)

    Also, since we added a docstring to the callback function, by default it
    will be extracted and used as the help text.

    Try `python example_56.py create Camila` vs
    `python example_56.py --verbose create Camila`
    """
    if verbose:
        print("Will write verbose output")
        state["verbose"] = True


if __name__ == "__main__":
    app()
