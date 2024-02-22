import typer

"""See https://typer.tiangolo.com/tutorial/commands/"""

"""
The preceding examples have all been creating a single function and 
passing it to `typer.run()`. This is a shortcut, under the hood Typer
converts it to a CLI application with `typer.Typer()` and executes it.

Now we need to create an explicitly create the application

I note that by default `--help` shows options for 
   --install-completion and
   --show-completion.
   
It might be nice to disable those.
"""

app = typer.Typer()


@app.command()
def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
