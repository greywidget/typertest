import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/commands/help/"""

# Rich Markdown
# If you set `rich_markup_mode="markdown"` when creating the `typer.Typer()`
# app, you will be able to use Markdown in the docstring
# Notice how you can use Markdown in the help text overwritten for the
# command `delete` just as before.

app = typer.Typer(rich_markup_mode="markdown")


@app.command()
def create(
    username: Annotated[str, typer.Argument(help="The username to be **created**")],
):
    """
    **Create** a new *shinny* user. :sparkles:

    * Create a username

    * Show that the username is created

    ---

    Learn more at the [Typer docs website](https://typer.tiangolo.com)
    """
    print(f"Creating user: {username}")


@app.command(help="**Delete** a user with *USERNAME*.")
def delete(
    username: Annotated[str, typer.Argument(help="The username to be **deleted**")],
    force: Annotated[bool, typer.Option(help="Force the **deletion** :boom:")] = False,
):
    """
    Some internal utility function to delete.
    """
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
