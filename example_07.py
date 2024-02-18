import typer
from rich.console import Console

"""Another example based on https://typer.tiangolo.com/tutorial/"""

# Looking at "standard error" output

err_console = Console(stderr=True)


def main():
    err_console.print("Here is something written to standard error")


if __name__ == "__main__":
    typer.run(main)
