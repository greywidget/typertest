import typer
from typing_extensions import Annotated

"""See https://typer.tiangolo.com/tutorial/commands/help/"""

# Rich Markdown and Markup
# If you have Rich installed you can configure your app to enable
# markup text with the parameter `rich_markup_mode`

# Checkout https://rich.readthedocs.io/en/stable/markup.html

# Then you can use more formatting in the docstrings and `help`
# parameter for CLI Arguments and CLI Options

# By default `rich_markup_mode` is `None` which disables any rich
# text formatting

# Check the help text below, there are a bunch of different things going on

app = typer.Typer(rich_markup_mode="rich")


@app.command()
def create(
    username: Annotated[
        str, typer.Argument(help="The username to be [green]created[/green]")
    ],
):
    """
    [bold green]Create[/bold green] a new [italic]shinny[/italic] user. :sparkles:

    This requires a [underline]username[/underline].
    """
    print(f"Creating user: {username}")


@app.command(help="[bold red]Delete[/bold red] a user with [italic]USERNAME[/italic].")
def delete(
    username: Annotated[
        str, typer.Argument(help="The username to be [red]deleted[/red]")
    ],
    force: Annotated[
        bool, typer.Option(help="Force the [bold red]deletion[/bold red] :boom:")
    ] = False,
):
    """
    Some internal utility function to delete.
    """
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
