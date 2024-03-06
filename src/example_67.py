import typer

"""See https://typer.tiangolo.com/tutorial/commands/context/"""

"""
Configuring the Context

You can pass configurations for the context when creating a command or callback

You can read more about this at: 
https://click.palletsprojects.com/en/7.x/api/#context

For example, you could keep additional CLI parameters not declared in your CLI
program with `ignore_unknown_options` and `allow_extra_args`

Then you can access those extra raw CLI parameters as a `list` of `str` in
`ctx.args`:
"""


app = typer.Typer()


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def main(ctx: typer.Context):
    """
    Try running with:
    --name Camila --city Berlin

    """

    for extra_arg in ctx.args:
        print(f"Got extra arg: {extra_arg}")


if __name__ == "__main__":
    app()
